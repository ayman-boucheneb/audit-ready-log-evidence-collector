import csv
import os
import re
from collections import Counter

# Config / thresholds
HIGH_FREQ_THRESHOLD = 200 
FAILED_BURST_THRESHOLD = 5
SENSITIVE_REPEAT_THRESHOLD = 3
SENSITIVE_PATHS = ("/admin", "/wp-admin", "/phpmyadmin", "/server-status", "/.env", "/.git/")



csv_folder = "outputs"
try:
    os.mkdir(csv_folder)
    print("Folder %s created!" % csv_folder)
except FileExistsError:
    print("Folder %s already exists" % csv_folder)
# Path to sample log
log_file = "logs/sample_30days.log"
summary_csv = 'outputs/summary.csv'
alerts_csv  = "outputs/alerts.csv"

# Define the regex pattern for Apache log entries
log_pattern = re.compile(
    r'(\S+)\s+'                 # IP address
    r'(\S+)\s+'                 # ident (usually -)
    r'(\S+)\s+'                 # user (usually -)
    r'\[([^\]]+)\]\s+'          # timestamp
    r'"(\S+)\s+(\S+)\s*(\S*)"\s+'  # method, path, protocol
    r'(\d{3})\s+'               # status
    r'(\S+)\s+'                 # bytes (number or -)
    r'"([^"]*)"\s+'             # referer
    r'"([^"]*)"'                # user-agent
)

fieldnames = ['record_type','ip','status','path','count']




with open (summary_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)
        

    try:
        with open(log_file, "r", encoding="utf-8", errors="replace") as f:
            total_lines = 0
            parsed_ok = 0
            parse_errors = 0

            ip_counts = Counter()
            status_counts = Counter()
            path_counts = Counter()

            failed_auth_by_ip    = Counter()
            sensitive_hits_by_ip = Counter()

            first_seen = {}
            last_seen  = {}
            


            for line in f:
                line = line.strip()
                total_lines +=1

                if not line:
                    continue  # skip blank lines

                m = log_pattern.match(line)
                if not m:
                    parse_errors +=1
                    # couldn't parse this line → skip or count an error
                    continue
                
                parsed_ok +=1
                timestamp   = m.group(4)
                source_ip   = m.group(1)
                method      = m.group(5)
                path        = m.group(6)
                status      = m.group(8)
                byte_count  = m.group(9)
                if byte_count == "-":
                    byte_count = ""
                user_agent  = m.group(11)

                ip_counts[source_ip] += 1
                status_counts[status] += 1
                path_counts[path] += 1

                # trackers
                if source_ip not in first_seen:
                    first_seen[source_ip] = timestamp
                last_seen[source_ip] = timestamp

                # Step 4 pre-counts for rules
                if status in ("401", "403") and "/api/auth" in path:
                    failed_auth_by_ip[source_ip] += 1
                if any(s in path for s in SENSITIVE_PATHS):
                    sensitive_hits_by_ip[source_ip] += 1


    except FileNotFoundError:
        print("The file you're trying to access doesn't exist:", log_file)

        
print(f"Total Lines={total_lines}, Successful Parses={parsed_ok}, Unsuccessful Parses={parse_errors}")    


#write summary.csv ONCE
with open(summary_csv, "w", newline="", encoding="utf-8") as out:
    w = csv.writer(out)
    w.writerow(["record_type", "ip", "status", "path", "count"])

    # IP rows
    for ip, count in ip_counts.most_common():
        w.writerow(["IP", ip, "", "", count])

    # Status rows
    for st, count in sorted(status_counts.items()):
        w.writerow(["STATUS", "", st, "", count])

    # Path rows
    for p, count in path_counts.most_common(50):
        w.writerow(["PATH", "", "", p, count])


alerts = []  # [timestamp, ip, event_type, severity, details]

# High Frequency Check
for ip, cnt in ip_counts.items():
    if cnt >= HIGH_FREQ_THRESHOLD:
        sev = "High" if cnt >= HIGH_FREQ_THRESHOLD * 2 else "Medium"
        alerts.append([first_seen.get(ip, ""), ip, "HighFrequency", sev, f"requests={cnt}"])

# Checking the failed login
for ip, fails in failed_auth_by_ip.items():
    if fails >= FAILED_BURST_THRESHOLD:
        alerts.append([first_seen.get(ip, ""), ip, "FailedLoginBurst", "High", f"failed_auth={fails}"])

#Checking paths
for ip, hits in sensitive_hits_by_ip.items():
    if hits >= SENSITIVE_REPEAT_THRESHOLD:
        sev = "High" if hits >= 5 else "Medium"
        alerts.append([first_seen.get(ip, ""), ip, "SensitivePathProbe", sev, f"sensitive_hits={hits}"])

with open(alerts_csv, "w", newline="", encoding="utf-8") as out:
    w = csv.writer(out)
    w.writerow(["timestamp", "ip", "event_type", "severity", "details"])
    w.writerows(alerts)

print(f"Wrote {summary_csv}")
print(f"Wrote {alerts_csv} ({len(alerts)} alerts)")
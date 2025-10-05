import csv
import os
import re
from collections import Counter

csv_folder = "outputs"
try:
    os.mkdir(csv_folder)
    print("Folder %s created!" % csv_folder)
except FileExistsError:
    print("Folder %s already exists" % csv_folder)

# Path to sample log
log_file = "logs/sample_30days.log"
csv_file_path = 'outputs/summary.csv'

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




with open (csv_file_path, mode='w', newline='', encoding='utf-8') as file:
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
                #timestamp   = m.group(4)
                source_ip   = m.group(1)
                #method      = m.group(5)
                path        = m.group(6)
                status      = m.group(8)
                #byte_count  = m.group(9)
                #if byte_count == "-":
                #    byte_count = ""
                #user_agent  = m.group(11)

                ip_counts[source_ip] += 1
                status_counts[status] += 1
                path_counts[path] += 1

            print(f"Total Lines={total_lines}, Successful Parses={parsed_ok}, Unsuccessful Parses={parse_errors}")    
            
            # IP rows (all IP counts)
            for ip, count in ip_counts.most_common():
                writer.writerow(['IP', ip, '', '', count])

            # STATUS rows (HTTP code totals)
            for status, count in sorted(status_counts.items()):
                writer.writerow(['STATUS', '', status, '', count])

            # PATH rows (top N paths so file isn't huge)
            for path, count in path_counts.most_common(50):
                writer.writerow(['PATH', '', '', path, count])

    except FileNotFoundError:
        print("The file you're trying to access doesn't exist:", log_file)
print("Top 10 IPs:")
for ip, cnt in ip_counts.most_common(10):
    print(f"  {ip:>15}  {cnt}")

print("\nHTTP Status counts:")
for st, cnt in sorted(status_counts.items()):
    print(f"  {st}: {cnt}")

print("\nTop 10 Paths:")
for p, cnt in path_counts.most_common(10):
    print(f"  {p:30}  {cnt}")
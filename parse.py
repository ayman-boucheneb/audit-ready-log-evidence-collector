import csv
import os
import re

csv_folder = "output"
try:
    os.mkdir(csv_folder)
    print("Folder %s created!" % csv_folder)
except FileExistsError:
    print("Folder %s already exists" % csv_folder)

# Path to sample log
log_file = "logs/apache_access.log"
csv_file_path = 'output/alerts.csv'

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

fieldnames = ['Timestamp' ,'Source IP' ,'Method', 'Path', 'Status', 'Bytes', 'User Agent']


with open (csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    try:
        with open(log_file, "r", encoding="utf-8", errors="replace") as f:
            total_lines = 0
            parsed_ok = 0
            parse_errors = 0
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

                writer.writerow({
                    'Timestamp':   timestamp,
                    'Source IP':   source_ip,
                    'Method':      method,
                    'Path':        path,
                    'Status':      status,
                    'Bytes':       byte_count,
                    'User Agent':  user_agent
                })
            print(f"Total Lines={total_lines}, Successful Parses={parsed_ok}, Unsuccessful Parses={parse_errors}")    
    except FileNotFoundError:
        print("The file you're trying to access doesn't exist:", log_file)

def detect_failed_logins(log_line):
    # TODO: add rule later
    return None

def detect_suspicious_ip(log_line):
    # TODO: add rule later
    return None

# detect_failed_logins(sample_line)
# detect_suspicious_ip(sample_line)
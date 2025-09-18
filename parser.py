import csv

# Path to sample log
log_file = "logs/apache_access.log"

# Step 1: Open log file
with open(log_file, "r") as f:
    lines = f.readlines()

# Step 2: Print first 5 lines (just to check input works)
for line in lines[:5]:
    print(line.strip())

def detect_failed_logins(log_line):
    # TODO: add rule later
    return None

def detect_suspicious_ip(log_line):
    # TODO: add rule later
    return None

sample_line = lines[1]  # pick the 2nd log entry
detect_failed_logins(sample_line)
detect_suspicious_ip(sample_line)
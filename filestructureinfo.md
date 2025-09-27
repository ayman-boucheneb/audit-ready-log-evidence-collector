log-parser/
│── README.md                 # project overview, setup, usage, output schema, implemented rules, next steps
│── parse.py                  # main parser: read logs, parse lines, (later) apply rules, write CSV
│── requirements.txt          # only libs you actually use (keep minimal; stdlib if possible)
│
├── logs/
│   └── apache_access.log     # sample/raw log file for testing
│
├── rules/
│   └── rules.md              # documentation of detection rules: names, triggers, severity mapping
│
├── output/
│   └── alerts.csv            # Step 2: parsed rows; Step 3+: flagged anomalies only
│
└── docs/
    ├── screenshots/          # terminal runs, sample CSV, optional Splunk views
    └── project-notes.md      # dev journal: decisions, pitfalls, tests, reflections


What each file/folder must do
README.md
Must include: What this is, prerequisites, setup/run steps, output schema, implemented rules list, example workflow, screenshots section, next steps.

parse.py
Must do:
Step 2: stream-read logs/apache_access.log, parse fields, write CSV (one row per line).
Step 3+: call rule functions (or inline logic), write only flagged events to CSV.
Always: clear errors if input missing; use relative paths; deterministic behavior.

requirements.txt
Only add packages you truly use (e.g., none, or maybe ipaddress if you rely on it). Keep it lean.

logs/apache_access.log
Small, controlled test set (10–100 lines) mixing normal + suspicious patterns.

rules/rules.md
Human-readable spec of each rule: Name → Condition → Fields used → Severity → Rationale.

output/alerts.csv
Step 2: Temporary container for parsed rows (see Step 2 schema below).
Step 3+: Final anomaly feed with agreed schema
    Timestamp,Source IP,Event Type,Severity,Details.

docs/screenshots/
Proof of runs (terminal, CSV open, optional Splunk).

docs/project-notes.md
Running log: assumptions, format quirks, tests, counts, follow-ups.
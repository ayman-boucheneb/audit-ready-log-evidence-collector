🖥️ Log Parser Project — Consolidated Brief (Final Structure Locked)
Aim (what this project is)
A mini SecOps engineering project that reads Apache access logs, parses each line, applies detection rules, and writes structured anomalies to a CSV that an analyst (or Splunk) can consume. It’s documented like a university assignment and polished for portfolio review.

What it should do (end state)
Read web server logs from logs/apache_access.log.
Parse each line into structured fields (IP, timestamp, request, status, etc.).
Detect suspicious activity with modular rules (auth failures, abusive frequencies, sensitive path probes)
Output only flagged anomalies to output/alerts.csv (Step 3 onward).
Document decisions, tests, and results (README + notes + screenshots).
Run deterministically on any machine with the repo.

Purposes (why it exists)
Practice Python parsing + basic threat detection.
Demonstrate SIEM-lite thinking without heavy platforms.
Produce analyst-ready outputs for dashboards.
Communicate like an engineer: clear docs, tests, evidence.







Steps (phased plan)
Step 1 — Skeleton (done earlier)
Confirm file can be read; basic loop; print sample lines.

Step 2 — Basic Parsing & Output (do today)
Turn raw lines into structured CSV rows (one row per log line).
Note: In Step 2 you temporarily write all parsed lines to output/alerts.csv. In Step 3 you’ll switch that file to flagged anomalies only (same filename; behavior changes).

Step 3 — First Detection Rules
Implement minimum rules and change behavior so output/alerts.csv contains only flagged events. Document rules and severity.

Step 4 — Quality & Evidence
Refactor for clarity, add screenshots, finalize docs, make runs deterministic.

Step 5 — Final Review & Commit
Small sample inputs/outputs included, README complete, tag v1.0.
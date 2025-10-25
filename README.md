# Log Analysis & Audit (Mini Project)

## Overview
This project is an **audit & security monitoring task**. It focuses on analysing 30 days of simulated Apache access logs to identify and evaluate potential security threats. The purpose of this project was to simulate a real-world scenario of detecting suspicious behaviour, using log data to highlight indicators of malicious activities. The project replicates how basic security monitoring and alerting can be performed using scripting methods and structured reporting.

## Aims & Objectives
- Understand how to analyse log data for suspicious patterns and indicators of compromise
- Parse raw Apache logs using Python to generate structured outputs
- Implement simple detection rules to highlight suspicious activity
- Document findings in a structured report

## Tools Used in Project:
- Python – to build the log parser, apply detection rules, and generate structured outputs
- CSV output – to store the results of the analysis in a clear and reusable format
- Splunk (attempted) – to visualise statistics and make the data easier to understand

## File & Folder Structure
- `README.md`: Serves as an introduction to the project. Explains the purpose, aim and structure of the project.
- `/logs`: folder containing the original log file used for the project
    - `sample_30days.log` - the main dataset that will be audited the "parse.py"
- `/outputs`: folder containing the output files produced by the parser
    - `summary.csv` - contains the traffic summary (IPs, status codes, paths)
    - `alerts.csv` - contains the detection alerts produced from suspicious activity
- `/docs`: folder containing project documentation
    - `Individual Report for Project.docx` - personal report with reflections and findings
    - `Log Parser Report.docx` - report about findings of the pased logs
    - `project-notes.ipynb` - personal notes taken throughout the project
- `parse.py`: python script used to parse the log file and generate outputs
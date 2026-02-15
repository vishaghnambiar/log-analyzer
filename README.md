# 📊 Log Analyzer (Python)

A lightweight Python project that analyzes system log files to extract useful insights such as user activity, common errors, and warning patterns.
This project demonstrates real-world backend data processing similar to tasks performed in DevOps and production debugging environments.

---

## 🚀 Features

* 🔍 Parses raw `.txt` log files
* 🧠 Uses **Regular Expressions (Regex)** to extract structured data
* 👤 Tracks most active users
* 🚨 Detects most frequent errors
* ⚠️ Summarizes warnings
* 📊 Generates a CSV report for further analysis
* ⚡ Fast and dependency-free (uses only Python standard library)

---

## 🛠️ Tech Stack

* **Python 3**
* `re` → Pattern matching & parsing
* `collections.Counter` → Data aggregation
* `csv` → Report generation

---

## 📁 Project Structure

```
log-analyzer/
│
├── log_analyzer.py     # Main script
├── login.txt           # Input log file
├── log_report.csv      # Auto-generated report (after running)
└── README.md
```

---

## 📄 Expected Log Format

The script works with logs formatted like:

```
YYYY-MM-DD HH:MM:SS LEVEL User: <username> <message>
```

### Example:

```
2026-02-10 10:15:32 INFO User: Rahul logged in
2026-02-10 10:16:01 ERROR User: Ankit failed login (Invalid Password)
2026-02-10 10:17:45 WARNING User: Rahul session timeout
```

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/log-analyzer.git
cd log-analyzer
```

### 2️⃣ Run the Script

```
python log_analyzer.py
```

---

## 📊 Sample Output

```
========= LOG ANALYSIS REPORT =========

User Activity:
Rahul: 3 actions
Ankit: 2 actions

Most Common Errors:
failed login (Invalid Password): 2 times

Total Log Entries: 8
Total Errors: 3
Total Warnings: 1
```

---

## 📁 Generated CSV Report

After execution, a file named:

```
log_report.csv
```

is created for use in Excel, Power BI, or other analytics tools.

| Category      | Value            | Count |
| ------------- | ---------------- | ----- |
| User Activity | Rahul            | 3     |
| Error         | Invalid Password | 2     |
| Warning       | Session Timeout  | 1     |

---

## 💡 What This Project Demonstrates

This project showcases skills relevant to:

* Backend Automation
* Log Processing Pipelines
* DevOps Monitoring
* Data Extraction from Unstructured Sources
* Debugging Production Systems
* Writing Maintainable CLI Tools

---

## 🎯 Learning Outcomes

* Transforming raw logs → structured insights
* Writing efficient regex patterns
* Automating repetitive analysis tasks
* Generating machine-readable reports
* Understanding how monitoring tools work internally

---

## 🔮 Future Improvements (Planned)

* Visualization dashboard (charts & trends)
* Real-time log streaming support
* Database integration
* REST API for log ingestion
* Containerized deployment (Docker)

---

## 👨‍💻 Author

**Vishagh Nambiar**

---

## 📜 License

This project is open-source and available under the MIT License.

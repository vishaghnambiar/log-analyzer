import re
from collections import Counter
import csv

# -----------------------------
# 1️⃣ Load Log File
# -----------------------------
log_file = "login.txt"

try:
    with open(log_file, "r") as file:
        logs = file.readlines()
except FileNotFoundError:
    print("❌ Log file not found. Make sure 'login.txt' exists.")
    exit()

# -----------------------------
# 2️⃣ Define Regex Pattern
# -----------------------------
pattern = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
    r'(?P<level>\w+) User: (?P<user>\w+) ?(?P<message>.*)'
)

# -----------------------------
# 3️⃣ Extract Data
# -----------------------------
users = []
errors = []
warnings = []
info_logs = []
timestamps = []

for line in logs:
    match = pattern.search(line)

    if match:
        data = match.groupdict()

        users.append(data["user"])
        timestamps.append(data["timestamp"])

        if data["level"] == "ERROR":
            errors.append(data["message"])

        elif data["level"] == "WARNING":
            warnings.append(data["message"])

        elif data["level"] == "INFO":
            info_logs.append(data["message"])

# -----------------------------
# 4️⃣ Analyze Data
# -----------------------------
user_activity = Counter(users)
error_count = Counter(errors)
warning_count = Counter(warnings)

# -----------------------------
# 5️⃣ Display Insights
# -----------------------------
print("\n========= 📊 LOG ANALYSIS REPORT =========\n")

print("👤 User Activity:")
for user, count in user_activity.most_common():
    print(f"{user}: {count} actions")

print("\n🚨 Most Common Errors:")
for error, count in error_count.most_common():
    print(f"{error}: {count} times")

print("\n⚠️ Warnings:")
for warn, count in warning_count.most_common():
    print(f"{warn}: {count} times")

print(f"\n🕒 Total Log Entries: {len(timestamps)}")
print(f"❌ Total Errors: {len(errors)}")
print(f"⚠️ Total Warnings: {len(warnings)}")

# -----------------------------
# 6️⃣ Export CSV Report
# -----------------------------
csv_file = "log_report.csv"

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Category", "Value", "Count"])

    for user, count in user_activity.items():
        writer.writerow(["User Activity", user, count])

    for error, count in error_count.items():
        writer.writerow(["Error", error, count])

    for warn, count in warning_count.items():
        writer.writerow(["Warning", warn, count])

print(f"\n✅ CSV Report Generated: {csv_file}")

# -----------------------------
# 7️⃣ Detect Suspicious Behavior (Bonus Logic)
# -----------------------------
print("\n🔎 Suspicious Activity Check:")

for user, count in user_activity.items():
    if count >= 3:
        print(f"⚠️ {user} has unusually high activity ({count} actions)")

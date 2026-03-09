# Cybersecurity Project
# Log Analyzer
# Author: @dilhayot-cyber
# GitHub: https://github.com/dilhayot-cyber

log_file = "server.log"

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            print("⚠️ Suspicious login attempt:", line)

#!/bin/bash

LOG_FILE="logs/server_health.log"

echo "==================================" >> $LOG_FILE
echo "Server Health Report - $(date)" >> $LOG_FILE
echo "==================================" >> $LOG_FILE

echo "" >> $LOG_FILE
echo "Disk Usage:" >> $LOG_FILE
df -h >> $LOG_FILE

echo "" >> $LOG_FILE
echo "RAM Usage:" >> $LOG_FILE
free -h >> $LOG_FILE

echo "" >> $LOG_FILE
echo "CPU Load:" >> $LOG_FILE
top -bn1 | grep "Cpu(s)" >> $LOG_FILE

echo "" >> $LOG_FILE
echo "System Uptime:" >> $LOG_FILE
uptime >> $LOG_FILE

echo "" >> $LOG_FILE
echo "Running Services:" >> $LOG_FILE
systemctl list-units --type=service --state=running >> $LOG_FILE

echo "" >> $LOG_FILE
echo "Health check completed!"

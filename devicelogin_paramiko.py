#! /usr/bin/python
 
import os
import paramiko
import xlsxwriter
import socket
 
username = ""
password = ""
 
# Opens files in read mode
f1 = open('hostfile','r')
f2 = open('commandfile','r')
 
# Creates list based on f1 and f2
devices = f1.readlines()
commands = f2.readlines()
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
data = []
for device in devices:
data.append([device])
for command in commands:
try:
ssh.connect(device, username=username, password=password, timeout=4)
stdin, stdout, stderr = ssh.exec_command(command)
output= stdout.read()
data[-1].append(output)
ssh.close()
except paramiko.AuthenticationException:
output = "Authentication Failed"
data[-1].append(output)
break
except socket.error, e:
output = "Connection Error"
data[-1].append(output)
break
data[-1] = tuple(data[-1])
f1.close()
f2.close()
 
#Create Workbook instance
book = xlsxwriter.Workbook('Workbook')
sheet = book.add_worksheet('Sheet1')
 
#Define and format header
header_format = book.add_format({'bold':True , 'bg_color':'yellow'})
textwrap = book.add_format()
textwrap.set_text_wrap()
header = ["", "",""]
for col, text in enumerate(header):
sheet.write(0, col, text, header_format)
 
 
# Now, let's write the contents
 
for row, data_in_row in enumerate(data):
for col, text in enumerate(data_in_row):
sheet.write(row + 1, col, text,textwrap)
 
book.close()
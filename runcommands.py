#!/usr/bin/env python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = '', username='root', password='password', timeout =  30)
while True:
      cisco_cmd = raw_input("Enter cisco router cmd:")
      stdin, stdout, stderr = ssh.exec_command(cisco_cmd)
      print stdout.read()
      if  cisco_cmd == 'exit': break
ssh.close()

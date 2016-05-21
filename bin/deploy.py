#!/usr/bin/python
# -* - coding: UTF-8 -* -  
#Author:Desmond Pan

import ConfigParser
import paramiko
#################################################################
#Generate a ConfigParser Object 
conf = ConfigParser.ConfigParser()
#Read the config file with object "conf" 
conf.read("./../config/server.conf")
#get the value for the host ,user, password

host = conf.get("dev_web","host")
user = conf.get("dev_web","user")
pswd = conf.get("dev_web","pswd")

#################################################################

#Generate a SSH Object
ssh = paramiko.SSHClient()
paramiko.util.log_to_file('./../log/deploy.log')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,22,user,pswd)
stdin,stdout,stderr = ssh.exec_command("ls -l /tmp")
for outmsg in stdout:
       print outmsg.strip('\n')
for errmsg in stderr:
       print errmsg.strip('\n')

ssh.close()
#################################################################

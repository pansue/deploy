#!/usr/bin/python
# -* - coding: UTF-8 -* -  
#Author:Desmond Pan

import ConfigParser
import paramiko
#################################################################
#Generate a ConfigParser Object 
conf = ConfigParser.ConfigParser()
#Read the config file with object "conf" 
conf.read("../config/server.conf")
#get the value for the host ,user, password
section=conf.sections()

################################################################
def	ssh_connect(host,user,pswd):
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
################################################################

print "Now,Let's begin to deploy!!!!"
print '''1. SAS_DEV_WEB
2. SAS_DEV_DB
3. SAS_QA_WEB
4. SAS_QA_DB
5. SAS_UAT_WEB
6. SAS_UAT_DB'''

env = input('please choose which environment to deploy:')


if env==1:
		host = conf.get("dev_web","host")
		user = conf.get("dev_web","user")
		pswd = conf.get("dev_web","pswd")

elif env == 2:
		host = conf.get("dev_db","host")
		user = conf.get("dev_db","user")
		pswd = conf.get("dev_db","pswd")
elif env == 3:
		host = conf.get("qa_web","host")
		user = conf.get("qa_web","user")
		pswd = conf.get("qa_web","pswd")
elif env == 4:
		host = conf.get("qa_db","host")
		user = conf.get("qa_db","user")
		pswd = conf.get("qa_db","pswd")
elif env == 5:
		host = conf.get("uat_web","host")
		user = conf.get("uat_web","user")
		pswd = conf.get("uat_web","pswd")
elif env == 6:
		host = conf.get("uat_db","host")
		user = conf.get("uat_db","user")
		pswd = conf.get("uat_db","pswd")
elif env == 7:
		host = conf.get("prod_web","host")
		user = conf.get("prod_web","user")
		pswd = conf.get("prod_web","pswd")
elif env == 8:
		host = conf.get("prod_db","host")
		user = conf.get("prod_db","user")
		pswd = conf.get("prod_db","pswd")
else:
		print "type error"

ssh_connect(host,user,pswd)
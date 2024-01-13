#!/bin/python3

import subprocess,sys



def find_emails(url):
	comand="python3"
	cmd = ["./spiderfoot/sf.py","-s"]+[url]+["-m","sfp_skymem"]
	p =subprocess.Popen([comand]+cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out,err = p.communicate() 
	out=out.decode('utf_8')
	lines = out.splitlines()
	new_list = lines[3:]
	filtered_lines = [line for line in lines if line.lower().startswith("email address")]
	filtered_lines2 = [line for line in lines if "@" in line]
	result = "\n".join(filtered_lines)

	email_list = []

	for string in new_list:
		parts = string.split("\t")
		email = parts[-1].strip()
		email_list.append(email)
	
	return(email_list)




import subprocess,sys
url= sys.argv[1]
comand="python3"
cmd = ["DirRunner.py","dir","-u"]+[url]+["-w","/usr/share/wordlists/dirb/common.txt"]



p=subprocess.Popen(["./bashhh"]+[url], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = p.communicate() 

"""import re
out=out.decode('utf-8')
matches = re.findall("GET", out)
print(matches)"""
print(out.decode('utf-8'))

"""if p.returncode == 0:
    with open("rep.txt", "r") as f:
        print(f.read())
f.close()

with open('rep.txt', 'r') as input_file, open('output_file.txt', 'w') as output_file:
    for line in input_file:
        if 'GET' in line:
            output_file.write(line)
output_file.close()
input_file.close()
#print(out.decode('utf-8'))
#print(err.decode('utf-8'))"""

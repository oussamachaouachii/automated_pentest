
#!/bin/python3
import subprocess,sys
domain= sys.argv[1]
p=subprocess.Popen(["./GooFuzz"]+["-e","pdf,bak,txt","-t"]+[domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = p.communicate() 
print(out.decode('utf-8'))
g=subprocess.Popen(["./GooFuzz"]+["-w","admin,config,/images/", "-t"]+[domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
outt,errr = g.communicate() 
print(outt.decode('utf-8'))

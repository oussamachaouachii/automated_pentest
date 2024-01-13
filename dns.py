import subprocess

def enumerate_subdomains_normal(domain):
    subdomains = []
    # Execute sublist3r command and capture output
    subprocess_output = subprocess.run(['sublist3r', '-d', domain],timeout=2000, capture_output=True)
    output_lines = subprocess_output.stdout.decode().splitlines()
    output_lines=output_lines[23:]
    for line in output_lines:
        subdomains.append(line)
    return subdomains 

def enumerate_subdomains_offensive(domain): 
	subdomains = []
        # Execute gobuster command and capture output
	subprocess_output = subprocess.run(['gobuster','dns','-w', '/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt','-d', domain, '-t' ,'50'], timeout=1500,capture_output=True)
	output_lines = subprocess_output.stdout.decode().splitlines()
	output_lines=output_lines[11:-4]
	for line in output_lines:
		subdomains.append(line)
	return subdomains

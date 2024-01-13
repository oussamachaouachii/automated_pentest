import nmap

nmScan = nmap.PortScanner()
args = "-T4"

def nmap_offensive(ipaddress):
    
    scanTechniques = [
    ("-sS", "SYN SCAN"),
    ("-sT", "CONNECT() SCAN"),
    ("-sA", "ACK SCAN"),
    ("-sW", "WINDOW SCAN"),
    ("-sM", "MAIMON SCAN")
    ]
    for technique in scanTechniques:
        f = open("rapport.html", 'a+')
        html = '''
                <pre>
        '''
        args = "-T4 -O -sV --script=vulners.nse --top-ports 100 " + technique[0]
        sc = nmScan.scan(ipaddress,arguments=args,timeout=100)
       
        sc = sc['scan']
       
        if sc[ipaddress].all_protocols():
            
            html = '''
                <h3> The scanned host is : </h3> <p>{ip} ({hostname})</p> 
            '''.format(ip=ipaddress, hostname=sc[ipaddress].hostname())
            f.write(html)
            if "tcp" in sc[ipaddress].all_protocols():
                
                html = '''<h3>Open TCP Ports :</h3>
                '''
                f.write(html)
                for port in sc[ipaddress]['tcp'].keys() :
                   if nmScan[ipaddress]['tcp'][port]['state'] == 'open':
                   
                    f.write("[[{port_number}]]<br>".format(port_number=str(port)))
                    for key,val in sc[ipaddress]['tcp'][port].items():
                        if key=="script":
                            if "vulners" in val.keys():
                                
                                f.write("""
                                <h3>Vulnerabilities :</h3>
                                    <pre>{vulns}</pre>
                                """.format(vulns=val["vulners"]))
                                
                            else:
                                
                                f.write("<h3>Vulnerabilities :</h3><p>none found</p>")
                        else:
                            
                            f.write("{key_string}  :  {val_string} <br>".format(key_string=key, val_string=val))
            if "udp" in sc[ipaddress].all_protocols():
                
                html = '''<h3>Open UDP Ports :<h3>
                '''
                f.write(html)
                for port in sc[ipaddress]['udp'].keys() :
                   if nmScan[ipaddress]['udp'][port]['state'] == 'open':
                    
                    f.write("[[{port_number}]]<br>".format(port_number=str(port)))
                    for key,val in sc[ipaddress]['udp'][port].items():
                        f.write("{key_string}  :  {val_string} <br>".format(key_string=key, val_string=val)) 
                        
            if "osmatch" in sc[ipaddress].keys():
                
                f.write("<h3>OS Discovery :<h3><br>")
                osGuessnumber = 0
                f.write('''
                    <table>
                      <tr>
                        <th>N°</th>
                        <th>Name</th>
                        <th>Accuracy</th>
                        <th>CPE</th>
                      </tr>
                ''')
                for osGuess in sc[ipaddress]["osmatch"]:
                    osGuessnumber += 1
                    f.write('''
                        <tr>
                            <td>{osNumber}</td>
                            <td>{name}</td>
                            <td>{accuracy}</td>
                            <td>{cpe}</td>
                        </tr>
                    '''.format(osNumber=osGuessnumber, name=osGuess["name"], accuracy=osGuess['accuracy'], cpe=osGuess['osclass'][0]['cpe'][0]))    
                f.write("</table>")                      
            break
        html = '''
            </pre>
        '''
        f.write(html)
        f.close()


def nmap_normal(ipaddress):
    scanTechniques = [
    ("-sS", "SYN SCAN"),
    ("-sT", "CONNECT() SCAN"),
    ("-sA", "ACK SCAN"),
    ("-sW", "WINDOW SCAN"),
    ("-sM", "MAIMON SCAN")
    ]
    for technique in scanTechniques:
        f = open("rapport.html", 'a+')
        html = '''

                <pre>
        '''
        f.write(html)
        args = "-T2 -O -sV --top-ports 100 " + technique[0]
        sc = nmScan.scan(ipaddress,  arguments=args)
        sc = sc['scan']
        if sc[ipaddress].all_protocols():
            html = '''
                <h3> The scanned host is : </h3> <h5>{ip} ({hostname})</h5> 
            '''.format(ip=ipaddress, hostname=sc[ipaddress].hostname())
            f.write(html)
            if "tcp" in sc[ipaddress].all_protocols():
                html = '''<h3>Open TCP Ports :</h3>
                '''
                f.write(html)
                for port in sc[ipaddress]['tcp'].keys() :
                   if nmScan[ipaddress]['tcp'][port]['state'] == 'open':
                    f.write("[[{port_number}]]".format(port_number=str(port)))
                    for key,val in sc[ipaddress]['tcp'][port].items():
                            f.write("{key_string}  :  {val_string} <br>".format(key_string=key, val_string=val))
            if "udp" in sc[ipaddress].all_protocols():
                html = '''<h3>Open UDP Ports :<h3>
                '''
                f.write(html)
                for port in sc[ipaddress]['udp'].keys() :
                   if nmScan[ipaddress]['udp'][port]['state'] == 'open':
                    f.write("[[{port_number}]]<br>".format(port_number=str(port)))
                    for key,val in sc[ipaddress]['udp'][port].items():
                        f.write("{key_string}  :  {val_string} <br>".format(key_string=key, val_string=val))
            if "osmatch" in sc[ipaddress].keys():
                f.write("<h3>OS Discovery :</h3><br>")
                osGuessnumber = 0
                f.write('''
                    <table>
                      <tr>
                        <th>N°</th>
                        <th>Name</th>
                        <th>Accuracy</th>
                        <th>CPE</th>
                      </tr>
                ''')
                for osGuess in sc[ipaddress]["osmatch"]:
                    osGuessnumber += 1
                    f.write('''
                        <tr>
                            <td>{osNumber}</td>
                            <td>{name}</td>
                            <td>{accuracy}</td>
                            <td>{cpe}</td>
                        </tr>
                    '''.format(osNumber=osGuessnumber, name=osGuess["name"], accuracy=osGuess['accuracy'], cpe=osGuess['osclass'][0]['cpe'][0]))    
                f.write("</table>")                      
            break
        html = '''
                </pre>
        '''
        f.write(html)
        f.close()
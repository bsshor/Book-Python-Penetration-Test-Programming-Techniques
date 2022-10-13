import sys
import nmap
if len(sys.argv) != 3:
    print("Usage : PortScan <IP>\n eg : ServiceScan 192.168.1.1 80")
    sys.exit(1)
target = sys.argv[1]
port = sys.argv[2]
nm = nmap.PortScanner()
nm.scan(target, port, "-sV")
for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print("port %s\t product %s" %
                  (port, nm[host][proto][port]["product"]))

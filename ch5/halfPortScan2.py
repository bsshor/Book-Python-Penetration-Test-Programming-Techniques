# 使用 nmap 实现TCP端口半开扫描
import sys
import nmap
if len(sys.argv) != 3:
    print("Usage: halfPortScan2 <IP Port>\n eg: halfPortScan2 192.168.11 80-445 ")
    sys.exit(1)
target = sys.argv[1]
port = sys.argv[2]
nm = nmap.PortScanner()
nm.scan(target, port)
for host in nm.all_hosts():
    print("---------------------------------------------------------")
    print(" Host : {0} {1} ".format(host , nm[host].hostname()))
    print(" State : {0} ".format(nm[host].state()))
    for proto in nm[host].all_protocols():
        print("-------------------------------------------")
        print("Protocol : {0}".format(proto))
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print(" port: {0}\tstate: {1}".format(port, nm[host][proto][port]))

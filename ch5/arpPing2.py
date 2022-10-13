# 使用nmap实现arp检测主机状态

import sys

if len(sys.argv) != 2:
    print(" Usage: arpPing < IP >\n eg: arpPing 192.168.1.1 or 192.168.237.0/24")
    sys .exit(1)
import nmap
nm = nmap.PortScanner()
nm.scan(sys.argv[1], arguments='-sn -PR')  # -PR 表示使用 ARP, -sn 表示只测试该主机的状态（这里是为了加快扫描速度）
for host in nm.all_hosts():
    print('----------------------------------------------------------------')
    print("Host: %s(%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())

# 使用nmap实现tcp 检测主机状态

import sys
if len(sys.argv) != 2:
    print(" Usage: tcpPing < IP >\n eg: arpPing2 192.168.1.1 or 192.168.237.0/24")
    sys .exit(1)

import nmap
nm = nmap.PortScanner()
nm.scan(sys.argv[1], arguments='-sT')  # Nmap 中使用 -sT 表示使用 TCP,但是这里不能使用 -sn 选项，因为这样会跳过端口扫描
for host in nm.all_hosts():
    print('----------------------------------------------------------------')
    print("Host: %s(%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())

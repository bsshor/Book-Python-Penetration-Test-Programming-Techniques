# 使用scapy实现使用arp检测主机状态

from scapy.all import srp, Ether, ARP  # type: ignore

import sys
if len(sys.argv) != 2:
    print(" Usage: arpPing < IP >\n eg: arpPing2 192.168.1.1")
    sys .exit(1)
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=sys.argv[1]), timeout = 2)
for snd, rcv in ans:
    print("Target is alive")
    print(rcv.sprintf("%Ether.src% - %ARP.psrc%"))  # type: ignore

import time
from scapy.all import *

list = open("dests.txt").readlines()

def ids():
    for x in list:
        packet = IP(dst=x,src="YOUR IP")/TCP(dport=999,sport=1234)/"NEVERGONNAGIVEYOUUP"
        send(packet)
        print("A PACKET HAS BEEN SENT TO " + x)
        time.sleep(2)
ids()

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

ping = Ether()/IP(dst="10.0.2.4")/ICMP()/Raw()
ping['Raw'].load = "Hello World"
srp1(ping, timeout = 1)

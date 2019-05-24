"""Imports main functions and executes the program"""

import logging
import os
import sys
from termcolor import colored
try:
	from scapy.all import *
except:
	print("Scapy not installed. Please install the package and then run this program")
	sys.exit()
import inputs as i
import Extracting_Parameters as log

#This will suppress all messages that have a lower level of seriousness than error messages, while running or loading Scapy
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)


# Checking if running on root privelleges
print("\nRunning program as root", end=' ')
i.loading_feature(0)

if os.geteuid() != 0:
	print(colored("[ERROR]", "red"))
	i.time.sleep(0.5)
	print(colored("** Please run this program as root **\n", "red"))
	sys.exit()
else:
	print(colored("[CHECK]", "green"))
	i.time.sleep(0.5)

# Welcome Graphic
print("\33[1;92m" + "---------                   ----------".center(os.get_terminal_size().columns)   + "\33[0m") 
print("\33[1;92m" + "  ********* Packet Sniffer *********  ".center(os.get_terminal_size().columns)    + "\33[0m")
print("\33[1;92m" + "---------                   ----------".center(os.get_terminal_size().columns) + "\n" + "\33[0m")
i.time.sleep(0.5) 

# Starting the application
try:
	# Taking user inputs
	i.user()
	
	# Running Sniff Process
	if i.proto == '3':
		sniff(iface = i.net_iface, count = int(i.pkts), timeout = int(i.timeout), prn = log.extract)
	elif i.proto == '1':
		sniff(iface = i.net_iface, filter = "arp", count = int(i.pkts), timeout = int(i.timeout), prn = log.extract)
	else:
		sniff(iface = i.net_iface, filter = "icmp", count = int(i.pkts), timeout = int(i.timeout), prn = log.extract)
	
	#Closing the program
	i.sniff_log.close()
	print(colored("Finishing capture", "green"), end=' ')
	i.loading_feature(0)
	print(colored("Exiting application", "green"))
	i.time.sleep(0.5)
	print(i.colored("Please check the log file for captured packets", "green"))
	
except KeyboardInterrupt:
	print("\n\nProgram Interrupted. . . Exiting\n")

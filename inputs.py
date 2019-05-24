""" Takes user inputs for the parameters to sniff """

import subprocess
import os
from termcolor import colored
import time
import re

def loading_feature(value):
	for i in range(3):
		print(".", end=' ', flush=True)
		time.sleep(0.5)
	print(" "*value, end=' ')
	
def user():
	# Setting important variables global to be able to use by other python calls outsode this function
	global net_iface
	global pkts
	global timeout
	global proto
	global sniff_log
	
	print(colored("### Please give your inputs ", "yellow"))
	
	while True:	
		# User input for interface
		net_iface = input(colored("\nEnter the interface to allow sniffing of packets (e.g. 'eth0/enp0s8'): ", "yellow"))
		
		# Verifying the interface exists and is UP
		os.system('ifconfig -a | grep %s > iface.txt' %net_iface) # listing all interface and extracting the one input by the user
		iface_file = open("iface.txt", 'r')
		iface_file.seek(0)
		try:
				temp = iface_file.readlines()[0] # first line of the 'ifconfig -a | grep' would exist if interface is present
				re.search("UP", temp).group()
				iface_file.close()
				os.system('rm iface.txt')
				break
		except:
				print(colored("Interface not found/ DOWN", "red"))
				iface_file.close()
				continue
		
	# Setting user input interface to promisc mode
	subprocess.call(["ifconfig", net_iface, "promisc"], stdout=None, stderr=None, shell=False)
	print(colored("%s set to PROMISC mode\n" %net_iface, "green"))
			
	
	# User input for number of packets to sniff
	while True:
		pkts = input(colored("Total packets to sniff [Type 0 for infinity] : ", "yellow"))
		try:
			if int(pkts) == 0:
				break
			elif int(pkts) > 0:
				break
			else:
				print(colored("Wrong input\n", "red"))
				continue
		except:
			print(colored("Wrong input\n", "red"))
			continue
		
	# User input for timeout parameter
	while True:
		timeout = input(colored("\nSet Timeout to [seconds] : ", "yellow"))
		try:
			if int(timeout) > 0:
				break
			else:
				print(colored("Wrong input\n", "red"))
				continue
		except:
			print(colored("Wrong input\n", "red"))
			continue
	
	# Protocols to filter
	while True:
		proto = input(colored("\nEnter protocol to filter (1- ARP | 2- ICMP | 3- BOTH) [1/2/3] : ", "yellow"))
		if (proto == '1') or (proto == '2') or (proto == '3'):
			break
		else:
			print(colored("Wrong input\n", "red"))
			continue
	
	# User input to create log file and creating one
	log_file = input(colored("\nEnter a name of the log file, if already exists/ to create one : ", "yellow"))
	
	while True:
		if os.path.isfile(log_file):
			break
		else:
			print(colored("Log file created . . . %s\n" %log_file, "green"))
			break
	
	sniff_log = open(log_file, 'a')
	print('\x1b[6;30;42m' + '\nCapturing Packets' + '\x1b[0m', end=' ')
	loading_feature(250)
	print("")
		
""" Extracts parameters from the packets and stores into the log file entered by user in inputs.py """

from datetime import datetime
import inputs as i

# Takes the packet and extracts required parameters to store into the log file
def extract(packet):

        # Getting current time
        now = datetime.now()

        # Printing output to log file
        if i.proto == '3':
                print("Time:" + str(now)[:19] + "   Protocol: ALL" + "   SMAC: " + packet[0].src + "   DMAC:" + packet[0].dst, file = i.sniff_log)
        elif i.proto == '1':
                print("Time:" + str(now)[:19] + "   Protocol: ARP" + "   SMAC: " + packet[0].src + "   DMAC:" + packet[0].dst, file = i.sniff_log)
        else:
                print("Time:" + str(now)[:19] + "   Protocol: ICMP" + "   SMAC: " + packet[0].src + "   DMAC:" + packet[0].dst, file = i.sniff_log)

  So I was able to create a LAN but I did it online because I couldn't get more devices to use on my network. I was able to use an online platform called Zerotier to create an
online LAN.

PLATFORM USED: Zerotier
DEVICES IN NETWORK: 2 [BOTH KALI SYSTEMS]
                    My system and an online one.
TOOLS USED: NMAP, LOCAL AREA NETWORK.

INSTALLATIONS:
NMAP:- sudo apt-get update && sudo apt-get install nmap
ZEROTIER:- curl -s 'https://raw.githubusercontent.com/zerotier/ZeroTierOne/main/doc/contact%40zerotier.com.gpg' | gpg --import && \  
           if z=$(curl -s 'https://install.zerotier.com/' | gpg); then echo "$z" | sudo bash; fi

OBJECTIVE: Scanning and Enumerating my Local Network with Nmap on Kali Linux.
           To ensure there aren't any weaknesses in my network.

Scanned all my ports and found at least 6 ports opened
Major ports open: PORT 21 AND PORT 22
As we can see from the zerotier installation gpg might have been included in it

COMMANDS USED ON NMAP:

nmap {IP ADDRESS}/24
  Expected Output: A list of devices on your network, their IP addresses, and the open ports.
  This was a basic scan on my local network.

nmap -p 80 {IP ADDRESS}/24
  Expected Output: A list of devices with port 80 open.
  This scan was targeted at a specific port(80).
                       
nmap -sV 192.168.1.0/24
  Expected Output: A detailed list of open ports and the services running on them, including version information.
  This scan was to detect the version of services running on the open ports.
                  
sudo nmap -O 192.168.1.0/24
  Expected Output: The operating system details of the devices on the network.
  This scan was to check what were the Operating Systems of the devices connected to the network.
                       
sudo nmap -A 192.168.1.0/24
    Expected Output: Comprehensive information about the devices on the network, including open ports, services, 
    versions, operating systems, and traceroute details.
    This was an aggressive scan using the -A option, which includes OS detection, version detection, script scanning, and traceroute.

OUTCOME:
  I was able to scan the network with the commands above and the results were shocking.
1. I found out I had some of my ports open which could be exploited.
2. Learnt how those ports could be exploited with the help of AI


                

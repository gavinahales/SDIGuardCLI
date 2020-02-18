import requests
import getpass
import sys

print("\n---SDIGuardCLI Beta---")
print("https://github.com/gavinahales/SDIGuardCLI")
print("\n")

#Check connection to firewall before proceeding.
try:
    onlinechk = requests.get("https://sdiguard.abertay.ac.uk:4100/")
    if onlinechk:
        pass
    else:
        print("ERROR: Couldn't reach the firewall. You might be offline or not connected to an Abertay SDI network.")
        sys.exit()
except Exception:
    print("ERROR: Couldn't reach the firewall. You might be offline or not connected to an Abertay SDI network.")
    sys.exit()
    
terms = """IMPORTANT INFORMATION : 
Please log on to the firewall with your Abertay credentials rather than the username 'admin'

This lab is for academic use only.

You are advised not to use the lab to log into anything else (e.g. Online-banking, social media etc.) as ethical hacking techniques are sometimes taught in this lab.

Always remember to logout at https://sdiguard.abertay.ac.uk:4100
You will be logged out automatically after 60mins.
"""

print(terms)

print("\nPlease confirm you have read the terms above. (Enter y to confirm).")

confirmTerms = input()

if confirmTerms.lower() != "y":
    print("You must read and accept the terms before using this tool.")
    sys.exit()

username=""
password=""

while(len(username) == 0):
    print("Enter your university username (without the @uad.ac.uk bit):")
    username = input()
while(len(password) == 0):
    print("Enter your password:")
    password = getpass.getpass()

authreq = requests.post("https://sdiguard.abertay.ac.uk:4100/wgcgi.cgi", data={"fw_username":username, "fw_password":password, "fw_domain":"uad.ac.uk","submit":"Login", "action":"fw_logon", "fw_logon_type":"logon", "redirect":"", "lang":"en-US"})

success = "You have been successfully authenticated" in authreq.text

if success:
    print("SUCCESS: You have been authenticated with the firewall.")
else:
    print("FAILED: It looks like something went wrong. Are you sure your password was correct?")
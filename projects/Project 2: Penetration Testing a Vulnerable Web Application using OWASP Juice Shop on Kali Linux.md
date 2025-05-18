# 🛡️ Web App Pentesting: OWASP Juice Shop (Docker-Based Lab)
##🔧 Tools Used
• Kali Linux
• OWASP Juice Shop
• Burp Suite
• Nmap
• DIRB Docker
• Docker
• UFW (Uncomplicated Firewall)


# ⚙️ Environment Setup
## INSTALLATION
### Docker:
  sudo apt install docker.io
  sudo systemctl start docker
  sudo systemctl enable docker
  sudo systemctl status docker

### OWASP JUICE SHOP DEPLOYMENT
  sudo docker pull bkimminich/juice-shop

I also had to ensure port 3000 was opened and not blocked by the firewall that I enabled from the last project
  sudo ufw allow 3000
  Now port 3000 is allowed and working.

### RUNNING THE OSWAP JUICE CONTAINER
  sudo docker run -d -p 3000:3000 bkimminich/juice-shop
Then I checked if the site was running (http://localhost:3000)

# TASKS PERFORMED
1. Identify open ports
2. SQL injection
3. Cross-Site Scripting (XSS)
4. File upload vulnerability
5. Directory Traversal
6. Cross-Site Request Forgery (CSRF)

# RESULTS

## 1. Identify open ports
So for this, I will use Nmap to scan for open ports.
I scanned it and it was the only open port 3000, which is the port hosting the OWASP Juice Shop server.

## 2. SQL Injection
So I'll use Burp Suite to run this attack on the website.

Ok so I can see all the missions on the OWASP Juice site and I would love to do all

## MISSION 1: FIND THE SCORE BOARD
**TYPE:** Reconnaissance / Hidden Path Discovery
**OBJECTIVE:** Access the hidden scoreboard page
**METHOD:** Inspected page source

You won't find a link to it in the navigation or sidebar. Finding the Score Board is itself one of the hacking challenges. This mission was easy because all I did was inspect the site and analyze the structure of the web page and I was able to score-board page, all I had to do was add score-board to the existing link and I got there 'http://localhost:3000/#/score-board' and that
was all. Over here I can see all the web penetration missions.


## MISSION 2: DOM XSS
**TYPE:** XSS
**OBJECTIVE:** Perform a DOM-based XSS attack

**Payload USED:**
 <iframe src="javascript:alert(`xss`)">

**OUTCOME:**
A small popup (alert box) appeared with the text 'xss'
  
So this specific attack is harmless but becomes very dangerous when a hacker injects malicious javascript code into the webpage. This shows the website is vulnerable to cross-site scripting(XSS).

**IMPLICATIONS:**
Proves the app is vulnerable to script injection

**DANGERS:**
1. Stealing cookies(session hijacking)
2. logging keystrokes
3. Redirecting users to malicious websites

## MISSION 3: BONUS PAYLOAD
**TYPE:** XSS
**OBJECTIVE:** Perform another DOM-based XSS attack

**PAYLOAD USED:**
<iframe style="border-radius:12px" 
        src="https://open.spotify.com/embed/track/0aB0v4027ukVziUGwVGYpG?utm_source=generator" 
        width="100%" height="152" 
        frameBorder="0" allowfullscreen="" 
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

**OUTCOME:** A song started playing on the target website page. Demostrated fun but realistic risk of XSS attack.


## MISSION 4: BULLY CHATBOT
**TYPE:** MISCELLANEOUS [Social Engineering / Automation]
**OBJECTIVE:** Obtain a coupon code from the support chatbot.

  So what I did here was that i created an account so I could get access to the chatbot. Ok from what I'm seeing, I have to spam the chatbot to get the coupon. I created a Python script to run this task for me so I could just automate it, but somehow I'm running into this problem, tried fixing it yesterday and it affected my OS, to prevent time wastage, I'm just going to upload the script but it works. So after spamming 'coupon please' to the chatbot, it eventually told me the coupon code which was 'n<Mich7ZKp'. Did this on my Chrome browser after Firefox gave me a lot of issues.

**OUTCOME:** Recieved coupon code 'n<Mich7ZKp'


## MISSION 5: PRIVACY POLICY
**TYPE:** MISCELLANEOUS [Basic Recon]
**OBJECTIVE:** Locate and read the privacy policy page.

Ok, so all I had to do in this mission was to find the privacy policy page.

**OUTCOME:** Successfully navigated and read the document.

## MISSION 6: CONFIDENTIAL DOCUMENT
**TYPE:** SENSITIVE DATA EXPOSURE
**OBJECTIVE:** Discover and access a hidden confidential file.

  So I will be using a tool called dirb to scan the site. So dirb is a web content scanner. It looks for existing or hidden web objects by launching a dictionary attack on a web server and analyzing the responses. I chose to use dirb and not Burp Suite because dirb is faster and will do the attack faster.

COMMAND USED:
dirb http://localhost:3000/

Found a list of subdomains but I was able to get the confidential file at 'http://localhost:3000/ftp'

**OUTCOME:** Located sensitive path 'http://localhost:3000/ftp' containing the document.



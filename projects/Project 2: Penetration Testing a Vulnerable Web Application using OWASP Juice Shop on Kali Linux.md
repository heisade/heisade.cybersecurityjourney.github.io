# TOOLS
1. KALI LINUX
2. OSWAP
3. BURPSUITE

# INSTALLATION
OSWAP:
  sudo apt install docker.io
  sudo systemctl start docker
  sudo systemctl enable docker
  sudo systemctl status docker
  sudo docker pull bkimminich/juice-shop

I also had to ensure port 3000 was opened and not blocked by the firewall that i enabled from the last project
  sudo ufw allow 3000
  Now port 3000 is allowed and working.

# RUNNING THE OSWAP JUICE CONTAINER
  sudo docker run -d -p 3000:3000 bkimminich/juice-shop
Then I checked if the site was running (http://localhost:3000)

# TASKS
1. Identify open ports
2. SQL injection
3. Cross-Site Scripting (XSS)
4. File upload vulnerability
5. Directory Traversal
6. Cross-Site Request Forgery (CSRF)

# RESUTS

# 1. Identify open ports
So for this, I will use Nmap to scan for open ports.
I scanned it and it was the only open port 3000, which is the port hosting the OWASP Juice Shop server.

# 2. SQL Injection
So I'll use Burp Suite to run this attack on the website.

Ok so I can see all the missions on the OWASP Juice site and I would love to do all

## MISSION 1: You won't find a link to it in the navigation or sidebar. Finding the Score Board is itself one of the hacking challenges.
  This mission was easy because all I did was inspect the site and analyze the structure of the web page and I was able to score 
board page, all I had to do was add score-board to the existing link and I got there 'http://localhost:3000/#/score-board' and that
was all.
  Over here I can see all the web penetration missions.





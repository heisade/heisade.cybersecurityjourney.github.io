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
So for this, I will be using Nmap to scan for open ports.
I scanned it and it was the only port 3000 that was open which is the port that was hosting the OWASP Juice Shop server.

# 2. SQL Injection
So I'll be using Burp Suite to run this attack on the website.

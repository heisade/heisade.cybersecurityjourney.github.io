import socket
import requests

RED = "\033[91m"
RESET = "\033[0m"

print(RED + r" _   _ _____ ___ ____    _    ____  _____ " + RESET)
print(RED + r"| | | | ____|_ _/ ___|  / \  |  _ \| ____|" + RESET)
print(RED + r"| |_| |  _|  | |\___ \ / _ \ | | | |  _|  " + RESET)
print(RED + r"|  _  | |___ | | ___) / ___ \| |_| | |___ " + RESET)
print(RED + r"|_| |_|_____|___|____/_/   \_\____/|_____|" + RESET)
print("\033[1;34m© 2025 heisade. All rights reserved.\033[0m\n")

print("\033[1;33mThis project and its contents are the intellectual property of heisade.\033[0m\n")

print("\033[1;32mBy using or contributing to this project, you agree to:\033[0m\n")

print("\033[1;37m1. Respect the copyright and licensing terms specified in this repository.")
print("2. Use the project’s code and content ethically and responsibly.")
print("3. Provide proper attribution when using or referencing this work.")
print("4. Not use this project for any illegal, harmful, or unethical activities.")
print("5. Follow the contribution guidelines if submitting changes or improvements.")
print("6. Acknowledge and respect the work of others used in this project by adhering to their respective licenses.\033[0m\n")

print("\033[1;36mThank you for supporting a respectful and ethical development community!\033[0m")


print(' ')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

host = input('Enter IP address you want to scan: ')
port = int(input('Enter Port you want to scan: '))

def PortScanner(port):
    if s.connect_ex((host, port)):
        print(f"Port {port} is closed!")
    else:
        print(f"Port {port} is open!")

PortScanner(port)


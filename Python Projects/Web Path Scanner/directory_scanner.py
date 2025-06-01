import requests


user_url = input("Enter url[Without a slash at the end]: ")
if "https://" in user_url:
    url = user_url
else:
    url = f"https://{user_url}"


try:    
    url_request = requests.get(url)
    directories_found = []
    directories_found_count = 0
    if url_request.status_code == 200:
        print(f"[🟢] Site connected successfully \nStatus Code: {url_request.status_code}\n")
    else:
        print("[❌] Connection failed")

except requests.RequestException as e:
    print(f"[❌] Request failed \nUnable to connect to: {url}\n")
    print(f"Error: {e}")

with open("directories.txt", "r") as f:
    directories = [line.strip() for line in f if line.strip()]

for directory in directories:
    complete_url = f"{url}/{directory}"

    try:
        response = requests.get(complete_url, timeout=10)

        if response.status_code < 400:
            directories_found.append(directory)
            directories_found_count +=1
            print(f"🟢 Directory: /{directory} found!")

        else:
            print(f"🔴 Directory: /{directory} not found!")

    except requests.RequestException as e:
        print(f"❌ Request failed for directory!\n")
        print(f"Error: {e}")


print("✅ Scan complete\n")
print(directories_found)
print(f"Directories Found: {directories_found_count} directories.")
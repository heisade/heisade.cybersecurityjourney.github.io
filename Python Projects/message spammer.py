import pyautogui
import time

#Settings
message = "coupon please"  # The message to type
repeat_count = 10  # Number of times to send the message
delay = 1  # Delay (in seconds) between messages

#Brief pause before starting (to switch to your target app)
print("You have 10 seconds to switch to your target application...")
time.sleep(10)

#Spamming loop
for i in range(repeat_count):
    pyautogui.typewrite(message)  # Type the message
    pyautogui.press("enter")  # Press Enter to send
    time.sleep(delay)  # Wait before sending the next message

print("Done!")
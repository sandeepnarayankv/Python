import time

time_in_s = int(input("Enter Time in Seconds: "))

while time_in_s > 0:
    time.sleep(1.0)
    time_in_s -= 1
    print(f"Remaining Seconds: {time_in_s}")
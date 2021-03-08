
# Format - f"{variable}"

b1 = "bread"
b2 = "ham"
b3 = "eggs" 
# format method 1:
print(f"For breakfast I had {b1}")
print(f"For breakfast I had {b2}")
print(f"For breakfast I had {b3}")

 
import time  # time is a built-in Python module #issue 1


def clock_time():
    count = 0
    start_time = time.time()

    while count < 1000:
        now = time.time()  # references the time function
        print(f'It has been {now - start_time} seconds since the loop started \n')
        count += 1


clock_time()


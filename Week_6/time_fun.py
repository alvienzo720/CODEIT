import time

start_time = time.time()

for i in range(1000):
    i += 1

end_time = time.time() - start_time
# print(end_time)

local_time = time.localtime()
while True:
    hr = local_time.tm_hour
    min = local_time.tm_min
    sec = local_time.tm_sec

    current_time = f"{hr}:{min}:{sec}"
    print(current_time)

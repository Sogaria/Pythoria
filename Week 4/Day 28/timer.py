import time as t

start = t.time()
while True:
    time_now = t.time() - start
    time_now = int(time_now)
    minutes = time_now // 60
    seconds = time_now % 60
    print(f"{minutes:02}:{seconds:02}")
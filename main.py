import time

limit = 5
requests = []

while True:
    now = time.time()
    requests = [r for r in requests if now - r < 10]

    if len(requests) >= limit:
        print("Rate limit exceeded!")
    else:
        requests.append(now)
        print("Request accepted")

    time.sleep(1)

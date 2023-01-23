import time

def search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
        return -1

items = range(1000000)

start = time.time()
search(items, 999999) # Procura pelo último item
stop = time.time()
print(stop-start)

start = time.time()
search(items, 499999) # Procura pelo item do meio
stop = time.time()
print(stop-start)

start = time.time()
search(items, 10) # Procura por um item no início
stop = time.time()
print(stop-start)
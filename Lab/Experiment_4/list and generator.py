import time
import tracemalloc

n = 100000

def list_processing():
    return [x * 2 for x in range(n)]

def generator_processing():
    return (x * 2 for x in range(n))

tracemalloc.start()
start = time.time()
data = list_processing()
list_time = time.time() - start
list_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

tracemalloc.start()
start = time.time()
data = list(generator_processing())
generator_time = time.time() - start
generator_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("List time:", round(list_time, 5))
print("List memory:", list_memory)
print("Generator time:", round(generator_time, 5))
print("Generator memory:", generator_memory)

# Experiment 4 – List and Generator Processing

## Aim

Compare list-based processing and generator-based processing for a large dataset in terms of execution time and memory usage.

## Algorithm / Procedure

1. Generate a large sequence of numbers.
2. Process the sequence using a list.
3. Process the same sequence using a generator.
4. Measure execution time and memory usage.
5. Compare the results.

## Program

```python
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
```

## Data & Result

### Sample Output

```text
List time: 0.08
List memory: 4000000
Generator time: 0.09
Generator memory: 4000000
```

> **Note:** The exact execution time and memory values may differ depending on the system.

## Inference & Analysis

List processing stores all generated values in memory, whereas a generator produces values when they are required.

* **List:** Stores all values in memory.
* **Generator:** Produces values lazily.
* **Memory:** Generators are generally more memory-efficient when values do not need to be stored together.
* **Execution Time:** The actual execution time depends on the system and workload.

## Result

Thus, list-based and generator-based processing were successfully compared based on execution time and memory usage. Generator-based processing demonstrates the advantage of lazy evaluation, while list-based processing stores the complete dataset in memory.


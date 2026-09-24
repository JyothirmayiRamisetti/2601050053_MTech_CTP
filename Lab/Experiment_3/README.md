# Experiment 3 – Stack and Queue Package

## Aim

Develop a reusable Python package implementing **Stack and Queue using type hints and dataclasses**.

## Algorithm / Procedure

1. Define a Stack using a list.
2. Implement `push` and `pop` operations.
3. Define a Queue using a list.
4. Implement `enqueue` and `dequeue` operations.
5. Use type hints and dataclasses.

## Program

```python
from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


@dataclass
class Queue(Generic[T]):
    items: list[T] = field(default_factory=list)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        return self.items.pop(0)


# Stack
stack = Stack[int]()
stack.push(10)
stack.push(20)

# Queue
queue = Queue[str]()
queue.enqueue("A")
queue.enqueue("B")

print("Stack pop:", stack.pop())
print("Queue dequeue:", queue.dequeue())
```

## Data & Result

### Output

```text
Stack pop: 20
Queue dequeue: A
```

## Inference & Analysis

The program successfully implements reusable **Stack and Queue** data structures using **dataclasses and type hints**.

* **Stack Push:** O(1)
* **Stack Pop:** O(1)
* **Queue Enqueue:** O(1)
* **Queue Dequeue:** O(n) for the list implementation.

## Result

Thus, a reusable Stack and Queue implementation was successfully developed using **Python dataclasses and type hints**.


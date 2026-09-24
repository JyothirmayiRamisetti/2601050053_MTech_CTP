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

stack = Stack[int]()
stack.push(10)
stack.push(20)

queue = Queue[str]()
queue.enqueue("A")
queue.enqueue("B")

print("Stack pop:", stack.pop())
print("Queue dequeue:", queue.dequeue())

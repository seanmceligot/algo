## Queue

### Python deque
✅O(1)
https://docs.python.org/3/library/collections.html#collections.deque
from typing import Deque
from collections import deque
`deque.append(item)`
`deque.popleft()`

### Python (`Queue`)**
✅O(1) Thread Safe
https://docs.python.org/3/library/queue.html#module-queue
https://docs.python.org/3/library/asyncio-queue.html
import threading
import queue
`queue.put(item)`
`queue.get()`

### Python List
❌O(n)
`list.append(item)`
`list.pop(0)`

### Rust VecDeque
✅O(1)
`vecdeque.push_back(item)`
`vecdeque.pop_front()`

### Rust Vec
❌O(n)
`vec.push(item)`
`vec.remove(0)`

## Stack

Recommend
Language/Type
Push Method
Pop Method

✅O(1)
**Python (List)**
`list.append(item)`
`list.pop()`

✅O(1)
**Python (`deque`)**
`deque.append(item)`
`deque.pop()`

✅O(1)
**Rust (`Vec`)**
`vec.push(item)`
`vec.pop()`

✅O(1)
**Rust (`VecDeque`)**
`vecdeque.push_back(item)`
`vecdeque.pop_back()`

* * *

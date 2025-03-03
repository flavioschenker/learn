# Algorithms
## 0️⃣1️⃣ Binary Search
### **time**: O(log n), **space**: O(1) iter. O(log n) rec.
Binary search works by repeatedly dividing the search space in half. Initially, the search space has size $n$. After each step, the size of the search space is halved. The process stops when only one element remains.

#### Proof
Let $k$ be the number of iterations required to reduce the search space to $1$. After the first iteration, the size of the search space is $\frac{n}{2}$. After the second iteration, the size is $\frac{n}{4}$, and so on. After $k$ iterations, the size of the search space is: 

$$\frac{n}{2^k} = 1$$
$$n = 2^k$$
$$k = \log_2 n$$

#### Code
```Python
def bs_iterative(nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return l
```
```Python
def bs_recursive(nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        def rec(l, r):
            if l > r:
                return l

            m = (l + r) // 2
            if nums[m] > target:
                return rec(l, m - 1)
            elif nums[m] < target:
                return rec(m + 1, r)
            else:
                return m

        return rec(l, r)
```

## 🐇🐢 Floyd’s Cycle Finding
### **time**: O(n), **space**: O(1)
Floyd's Cycle Finding Algorithm (also known as Tortoise and Hare) is used to detect a cycle in a sequence of values, such as in a linked list. The algorithm works by using two pointers that move at different speeds. One (the "tortoise") moves one step at a time, while the other (the "hare") moves two steps at a time. If a cycle exists, the hare and tortoise will eventually meet.
#### Code
```Python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```


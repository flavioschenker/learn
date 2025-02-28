# 📖 Learning every day
This is my personal repository and cheatsheet for learning statistics, algorithms, data structures, and more.


# 👨‍💻 Leetcode problems
Below is a summary of the LeetCode problems I have solved.

My Roadmap:
1) Arrays ✅
2) Stack 🚧
3) Two Pointers
4) Binary Search
5) Sliding Window
6) Linked List
7) Trees
8) Heaps / Queues
9) Backtracking
## Easy Array Problems
### 🧩 88. Merge Sorted Array
#### **Problem**
There are two non-decreasing integer lists n1, n2. n1 has m and n2 k non-zero elements. n1 is padded with zeros so it is of length n+m.
#### **Task**
Sort the two lists inplace in n1, such that it is non-decreasing
#### **Example**
Input:  
n1 = [1,2,3,0,0,0], m = 3, n2 = [2,5,6], k = 3  
Output:  
[1,2,2,3,5,6]
#### **Solution idea:**
Start sorting from the **right** and fill n1 from the right by comparing the rightmost value of n1 and n2 with **pointers** p1 and p2. Decrease the corresponding pointer.
#### **Solution code:**
Python3
```Python
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m-1
    p2 = n-1
    r = m+n-1

    while p2 >= 0:
        if nums1[p1] >= nums2[p2] and p1 >= 0:
            nums1[r] = nums1[p1]
            p1 -= 1
        else:
            nums1[r] = nums2[p2]
            p2 -= 1
        r -= 1
```
C++
```cpp
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int p1 = m-1;
    int p2 = n-1;
    int r = n+m-1;
    while (p2 >= 0) {
        if (p1 >= 0 && nums1[p1] >= nums2[p2])  {
            nums1[r] = nums1[p1];
            p1--;
        } else {
            nums1[r] = nums2[p2];
            p2--;
        }
        r--;
    }
}
```

### 🧩 27. Remove Element
#### **Problem**
There is an integer s and an array of integers n.
#### **Task**
Remove all occurences of s in n and return the number of values != s.
#### **Example**
Input:  
n = [0,1,2,2,3,0,4,2], s = 2  
Output:  
5, [0,1,4,0,3]
#### **Solution idea:**
Simply iterate over n and use a **counter** c that only increases when value != s. Set the **next non s** to c.
#### **Solution code:**
```Python
def removeElement(nums: List[int], val: int) -> int:
    c = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[c] = nums[i]
            c += 1
    return c
```

### 🧩 26. Remove Duplicates from Sorted Array
#### **Problem**
There is an non-decreasing array n.
#### **Task**
Remove all duplicate values in n and return the number of unique values k in n. The first k values should be sorted in-place in n.
#### **Example**
Input:  
n = [0,0,1,1,1,2,2,3,3,4]  
Output:  
5, [0,1,2,3,4]
#### **Solution idea:**
Simply iterate over n and keep track of the **biggest encountered value** t. Use a **counter** c that only increases when n[i] > t. 
#### **Solution code:**
```Python
def removeDuplicates(nums: List[int]) -> int:
    t = nums[0]
    c = 1
    for i in range(len(nums)):
        if nums[i] > t:
            t = nums[i]
            nums[c] = nums[i]
            c += 1
    return c
```

### 🧩 169. Majority Element
#### **Problem**
There is an array n.
#### **Task**
Find the majority element (most frequent element in the array) in O(n) time and O(1) space.
#### **Example**
Input:  
n = [2,2,1,1,1,2,2]  
Output:  
2
#### **Solution idea:**
This solution uses the Boyer-Moore Voting Algorithm. The idea is to first set the first element in the array as majority and initiate a counting value c. Iterate over n and if there is a non majority element encountered decrease c otherwise increase it. The intuition is that only the majority element does not reach zero once in the iteration because it is present in more than 50% of the elements.
#### **Solution code:**
```Python
def majorityElement(nums: List[int]) -> int:
    major = nums[0]
    c = 0
    for num in nums:
        if num == major:
            c += 1
        else:
            c -= 1
        
        if c < 1:
            major = num
            c = 1
    return major
```

### 🧩 121. Best Time to Buy and Sell Stock
#### **Problem**
There is a price array n.
#### **Task**
Find the best possible profit by finding the best entry and exit point/value in the array and return the maximum profit.
#### **Example**
Input:  
n = [7,1,5,3,6,4]  
Output:  
5
#### **Solution idea:**
This solution calculates the profit p in every step, relative to the current entry price l. When the profit falls below zero, a new entry l is set. The best ever profit m is also stored.
#### **Solution code:**
```Python
def maxProfit(prices: List[int]) -> int:
    p = 0 # current profit
    m = 0 # best profit
    l = 10**4 # current low
    for price in prices:
        p = price - l
        if p <= 0:
            l = price
        if p > m:
            m = p
    return m
```


## Medium Array Problems
### 🧩 80. Remove Duplicates from Sorted Array 2
#### **Problem**
There is an non-decreasing array n.
#### **Task**
Remove duplicate values in n such that each value appears at most twice in-place. The relative order should be kept the same.
#### **Example**
Input:  
n = [0,0,1,1,1,1,2,3,3]  
Output:  
7, [0,0,1,1,2,3,3]
#### **Solution idea 1:**
I iterate over n using **two pointers**, c and j, while keeping track of the largest encountered value in t. If num > t (a new number), I store it at position c and increment c. Otherwise, if num <= t, there is **still room** for a second occurrence, and pointer j ensures that at most two instances of the number are stored. If j<2, meaning there is still space for another occurrence, I also store num at c and increment c.
#### **Solution code 1:**
```Python
def removeDuplicates(nums: List[int]) -> int:
    c = 0
    t = -10**5
    j = 0

    for num in nums:
        if num > t:
            j = 1
            t = num
            nums[c] = num
            c += 1
        else:
            if j < 2:
                nums[c] = num
                c += 1
                j += 1
    return c
```
#### **Solution idea 2:**
This is not my solution, but the slightly faster master solution from LeetCode. I iterate over n and store a pointer k=2. I only increase k when n[i] is a new number that differs from n[k-2]. Unlike in the easier version of the problem, I compare with position k-2 instead of k, because this allows for duplicates at k-1. By doing this, I ensure that I don't store a third element at k.
#### **Solution code 2:**
```Python
def removeDuplicates(nums: List[int]) -> int:
    k = 2
    for i in range(2,len(nums)):
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1
    return k
```

### 🧩 189. Rotate Array
#### **Problem**
There is an array n and an integer k.
#### **Task**
Rotate the array to the right by k steps.
#### **Example**
Input:  
n = [1,2,3,4,5,6,7], k = 3
Output:  
[5,6,7,1,2,3,4]
#### **Solution idea 1**
Trivial solution pop the last element and insert it at the beginning k times. Bad time and space complexity.
#### **Solution code 1:**
```Python
def rotate(nums: List[int], k: int) -> None:
    for i in range(k):
        o = nums.pop()
        nums.insert(0, o)
```
#### **Solution idea 2**
This solution relies on symmetry. Rotating an array is equivalent to reversing the entire array, then splitting it into two parts, left (first k elements) and right (remaining) and reversing each part individually. The initial reversal moves the first k elements to the end, but in reverse order, which is corrected by the second step. An edge case arises when k is greater than n, making the code ineffective. However, rotating an array of n elements by n results in the same array. Therefore, we only need to rotate it by k modulo n. For example, if k is 27 and n is 12, after 24 rotations (which form two full cycles), the array returns to its original state. This means only three additional rotations are needed.
#### **Solution code 2:**
```Python
def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    # reverse whole array
    for i in range(n//2):
        t = nums[i]
        nums[i] = nums[n-i-1]
        nums[n-i-1] = t
    # reverse left
    for i in range(k//2):
        t = nums[i]
        nums[i] = nums[k-i-1]
        nums[k-i-1] = t
    # reverse right
    for i in range((n-k)//2):
        t = nums[i+k]
        nums[i+k] = nums[n-i-1]
        nums[n-i-1] = t
```

### 🧩 122. Best Time to Buy and Sell Stock 2
#### **Problem**
There is a price array n.
#### **Task**
Find the best possible profit. You can hold maximum of 1 position. You can enter and exit anytime.
#### **Example**
Input:  
n = [7,1,5,3,6,4]  
Output:  
7
#### **Solution idea**
Just keep track of the price delta on each day. Begin on the second day and if the delta is positive just add it to the profit.
#### **Solution code:**
```Python
def maxProfit(prices: List[int]) -> int:
    p = 0
    for i in range(1,len(prices)):
        delta = prices[i] - prices[i-1]
        if delta > 0:
            p += delta
    return p
```

## Easy Two Pointers Problems
### 🧩 125. Valid Palindrome
#### **Problem**
There is a string of ASCII characters s.
#### **Task**
Filter s to only alphabetical characters a-Z and numbers and set all lowercase.  
Check if the filtered string is a palindrome.
#### **Example**
Input:  
s = "A man, a plan, a canal: Panama"  
f = "amanaplanacanalpanama"  
Output:  
true
#### **Solution idea**
First loop once over the string O(n) to filter it with standard Python methods. Then use two pointers l and r to traverse it from left and right symmetricaly O(n). As soon as the first non-equal characters are found return false, if nothing found return true.
#### **Solution code:**
```Python
def isPalindrome(s: str) -> bool:
    f = ''.join([char.lower() for char in s if char.isalnum()]) # O(n)
    l = 0
    r = len(f)-1
    while l<r: # O(n)
        if f[l] != f[r]:
            return False
        l += 1
        r -= 1
    return True
```

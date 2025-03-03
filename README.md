# 📖 Learning every day
This is my personal repository and cheatsheet for learning statistics, algorithms, data structures, and more.


# 👨‍💻 Leetcode problems
Below is a summary of the LeetCode problems I have solved.

## Roadmap
My Roadmap:

1) Array & String ✅
2) Stack ✅
3) Two Pointers ✅
4) Binary Search 🚧
5) Sliding Window
6) Linked List
7) Trees
8) Heaps / Queues
9) Backtracking
10) Tries

## Summary
|Problem|Solution
|---|---|
|cyclic shift an array      |flip two times with two pointer|
|find a loop in linked-list |tortoise and hare algorithm|
|merge sorted array         |pointer from right|
|find majority element      |boyer-moore algorithm|
|find best profit           |drag entry down if profit<0|
|find common prefix         |sort and compare only first and last|
|optimize walls/pairs       |two pointer, reduce weaker pointer|


## Easy Array & String Problems
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


### 🧩 58. Length of Last Word
#### **Problem**
There is a string s consisting of words and spaces.
#### **Task**
Find the length of the last word.
#### **Example**
Input:  
s = "Hello World"    
Output:  
5
#### **Solution idea:**
Start iteration from right and begin count as soon as first non-space character is encountered until a space is found.
#### **Solution code:**
```Python
def lengthOfLastWord(s: str) -> int:
    n = len(s)-1
    count = 0
    start = False
    for i in range(n, -1, -1):
        if s[i] == " " and start:
            return count
        if s[i] != " ":
            start = True
            count += 1
    return count
```


### 🧩 14. Longest Common Prefix
#### **Problem**
There is an array of strings s.
#### **Task**
Find the longest common prefix.
#### **Example**
Input:  
s = ["flower","flow","flight"]  
Output:  
"fl"  
#### **Solution idea:**
First sort array alphabetical and then compare **only the first and last** element.
#### **Solution code:**
```Python
def longestCommonPrefix(strs: List[str]) -> str:
    strs = sorted(strs) # nlogn
    l = strs[0]
    r = strs[-1]
    a = ""
    for i in range(min(len(l),len(r))):
        if l[i] != r[i]:
            return a
        a += l[i]
    return a
```


## Medium Array & String Problems
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

### 🧩 392. Is Subsequence
#### **Problem**
There are two strings s and t. s is a subsequence of t if s is formed of t by deleting some or none of the characters of t without disturbing the relative order.
#### **Task**
Return true if s is a subsequent of t, otherwise false.
#### **Example**
Input:  
s = "abc", t = "ahbgdc"  
Output:  
true
#### **Solution idea**
Loop over all characters of s and try to find the character using two pointers. If found increase p1. In each round increase p2. If at some point p2 reaches it's end before all characters of s are checked, return false. Otherwise true.
#### **Solution code:**
```Python
def isSubsequence(s: str, t: str) -> bool:
    p1 = 0
    p2 = 0
    while p1 < len(s):
        if p2 >= len(t):
            return False
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1
    return True
```

## Medium Two Pointers Problems
### 🧩 167. Two Sum 2 - Input Array Is Sorted
#### **Problem**
There is a non-decreasing array n with integer values and a target integer t.
#### **Task**
Find two values such that they add up to the target t and return their indices. There is exactly one solution. The two indices should not be the same.
#### **Example**
Input:  
n = [2,7,11,15], t = 9  
Output:  
[1,2]
#### **Solution idea 1**
Trivial solution: loop over array twice. Constant space but very very bad time complexity O(n^2). Fails submission anyways, due to timeout.
#### **Solution code 1**
```Python
def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]     
```
#### **Solution idea 2**
This solution runs in O(n) and has constant space complexity O(1). The idea is to use two pointers left and right. When the sum of the two pointers is greater then t, decrement the right pointer. If too small, increment the left pointer. This works because the array is sorted.
#### **Solution code 2**
```Python
def twoSum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1,r+1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1    
```

### 🧩 11. Container With Most Water
#### **Problem**
There is an array h with n elements that contain wall height values.
#### **Task**
Find the best wall pair that holds the most amount of water by forming a container with the x axis (indices apart).
#### **Example**
Input:  
h = [1,8,6,2,5,4,8,3,7]
Output:  
49
#### **Solution idea**
The trivial approach is to compare each wall with every other wall, but this results in a time complexity of O(n^2). Instead, we can use a more efficient scanning method that optimizes for the best wall pair. This can be achieved with two pointers, one starting from the left and the other from the right. We move the pointer pointing to the shorter wall inward since a taller wall has the potential to hold more water. We systematically identify the best wall pairs while scanning efficiently. This approach ensures that we find the optimal water levels in a much more efficient manner, as we naturally converge on the tallest wall pair in the array.
#### **Solution code**
```Python
def maxArea(height: List[int]) -> int:
    n = len(height)
    l = 0
    r = n-1
    w = 0
    while l < r:
        h_l = height[l]
        h_r = height[r]
        x = r-l
        if h_l < h_r:
            t = h_l*x
            l += 1
        else:
            t = h_r*x
            r -= 1
        if t > w:
            w = t
    return w
```

## Easy Linked List Problems
### 🧩 141. Linked List Cycle
#### **Problem**
There is the header h of a one-directional linked list.
#### **Task**
Return true if the ll contains a cycle, false otherwise.
#### **Example**
Input:  
head = [3,2,0,-4,2,0,-4,...]  
Output:  
true
#### **Solution idea 1**
Trivial solution: Store the memory of each encountered node in a hashmap. As soon as a dublicate is found return true. O(n) space complexity.
#### **Solution code 1**
```Python
    def hasCycle(head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        check = {}
        while head.next is not None:
            if id(head) in check:
                return True
            else:
                check[id(head)] = 1
            head = head.next
        return False   
```
#### **Solution idea 2**
Use the Tortoise and Hare algorithm: Initiate two pointers, one moving slowly (one step at a time) and one moving fast (two steps at a time). If the linked list has no cycle, the fast pointer will reach the end, and the two pointers will never meet. However, if there is a cycle, the fast pointer will eventually catch up to the slow pointer, confirming the presence of a cycle.
#### **Solution code 2**
```Python
    def hasCycle(head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```
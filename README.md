# 📖 Learning every day
This is my personal repository and cheatsheet for learning statistics, algorithms, data structures, and more.


# 👨‍💻 Leetcode problems
Below is a summary of the LeetCode problems I have solved.
## Easy Array Problems
### 88. Merge Sorted Array
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
```Python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
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

### 27. Remove Element
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
def removeElement(self, nums: List[int], val: int) -> int:
    c = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[c] = nums[i]
            c += 1
    return c
```

### 27. Remove Duplicates from Sorted Array
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
def removeDuplicates(self, nums: List[int]) -> int:
    t = nums[0]
    c = 1
    for i in range(len(nums)):
        if nums[i] > t:
            t = nums[i]
            nums[c] = nums[i]
            c += 1
    return c
```
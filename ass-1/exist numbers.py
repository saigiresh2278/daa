nums1 = [2, 3, 2]
nums2 = [1, 2]
answer1 = sum(1 for num in nums1 if num in nums2)  
answer2 = sum(1 for num in nums2 if num in nums1)  
result = [answer1, answer2]
print(result)  

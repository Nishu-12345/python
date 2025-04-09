# sum of even numbers in list

nums = [1,2,3,4,5,28,30,97]
even_sum = sum(num for num in nums if num%2==0)
print("sum of even numbers:",even_sum)

# convert list to tuple and find maximum value
nums = [1,4,2,78,33,76,35]
nums2 =tuple(nums)
print("list convert to tuple:", nums)

max_value =max(nums)
print("maximum value in tuple:",max_value)
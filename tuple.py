# # nums =(1,2)
# # a,b = nums
# # print(a,b)
nums =(1,2,3,4,5)
print(nums)
print(nums[1])
print(nums[-1])
print(nums[1:4])
nums =(1,2,3,4,5)
res =[]
for n in nums:
    res.append(n*n)
print(res)

# nums =(1,2)
# nums[1] = 20
# print(nums)

list = [1,2,3,4,5]
tup = (1,2,3)
dist={"key":"value"}
stu ={"name":"nishu", "age": 16}
# # print(stu["name"])
# # print(stu["age"])
# # print(stu.get("age"))
# # print(stu.get("xyz", "404"))
# # modification tuple
# # stu["age"]= 16
# # print(stu)
# # del stu["age"]
# # print(stu)
# stu ={"name":"nishu", "age": 16,"add":"lodhipur", "loc": "12"}
print(stu.keys())
print(stu.values())
print(stu.items())
for k, v in stu.items():
    print(k,v)
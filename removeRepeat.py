nums = [2,3,2,5,3,6,5,7]
num=[]
for i in nums:
    if i not in num:
        num.append(i)
print(num)
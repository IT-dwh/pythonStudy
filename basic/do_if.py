# 注意：
# input 返回的是字符串
# 必须通过int()讲字符串转换为整数
# 才能用于数值比较

age = int(input("input your age:"))
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

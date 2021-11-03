str = "zhangsan"

for temp in str:
    print(temp)
    
print("=========")

name = input("请输入姓名:")
age = int(input("请输入年龄:"))
sex = input("请输入性别:")

print("======================")
print("姓名:%s"%name,end="")
print("年龄:%d"%age,end="")
print("性别:%s"%sex)
print("======================")
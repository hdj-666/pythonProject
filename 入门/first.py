# m=input("请输入密码: ")
# n=input("请输入取款金额：")
# s=10000-int(n)
# print(f"还剩：{s}")
# a=float(input("请输入一个数"))
# print(f"{a}不在10-20之间： " , a<10 or a>20)
# accout="123456"
# password="6666"
# a=input("请输入用户名：")
# b=input("请输入密码：")
# if a == accout and b == password:
#     print(f"登入成功！")
#     print()
# else:
#     print(f"登入失败！")
#     print(f"密码或用户有误！")
# year=float(input("请输入年份："))
# if year % 4 == 0 and year % 400 == 0:
#     print(f"是闰年！")
# else:
#     print(f"不是闰年！")
# b=1000
# print(f"{b+year}")
# i=0
# while i<10 :
#     print(f"成立")
#     i+=1
# else:
#     print(f"结束")
# a=1
# sum=0
# while a<=100 :
#     if a %2 ==0 :
#         sum= sum+a
#     a += 1
#
# print(f"和为: {sum}")
# msg=input("请输入要遍历的字符串")
# for i in msg:
#     print(i)
# else:
#     print("结束")
# sum=0
# for i in range(100,501):
#     if i % 3 ==0 :
#         sum += i
# print(sum)
# m=int(input("请输入长："))
# n=int(input("请输入宽："))
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print("\n")
# for i in range(9):
#     for j in range(i+1):
#         print(f"{j+1} * {i+1} = {(j+1)*(i+1)}" , end="\t")
#     # print()

# m=int(input("请输入长："))
#
# for j in range(1,m+1):
#     for i in range(1,j+1):
#         print("*", end="\t")
#     print()

# import random
# rand_num=random.randint(1,100)
# while True:
#     num=int(input("请输入猜的数字："))
#     if num < rand_num:
#         print("猜小了！")
#     elif num >rand_num:
#         print("猜大了！")
#     else:
#         print(f"猜对了随机数为{rand_num}")
#         break

#
# list_num=[]
# for i in range(1,21):
#     list_num.append(i**2)
# print(list_num)

# list_num=[i**2 for i in range(1,21)]
# print(list_num)

dict1={"小明": 22,"小华": 33,"小李":66}
# print(dict1)
# # print(type(dict1))
# score=dict1["小明"]
# print(score)
# e=dict1.pop("小李")
# print(dict1)
# print(e)
# e=dict1.get("小李")
# print(e)
# list_key=[]
# list_key=dict1.keys()
# print(list_key)

# for key in dict1.keys():
#     print(f"{key}:{dict1[key]}")
mean='''
###########购物车系统##############
#          1.添加购物车           #
#          2.修改购物车           #
#          3.删除购物车           #
#          4.查询购物车           #
#          5.退出购物车           #
#################################
'''

shoppingcar={}
while True:
    print(mean)
    num=input("请输入操作：")
    match num:
        case "1":
            good_name=input("请输入物品名称：")
            if good_name in shoppingcar:
                print("已有商品！")
                continue
            good_price=input("请输入物品价格：")
            good_num=input("请输入物品数量：")
            shoppingcar[good_name]={"price":good_price,"num":good_num}
            print("添加成功！")
        case "2":
            good_name = input("请输入修改物品名称：")
            if good_name not in shoppingcar:
                print("物品不存在！")
                continue
            good_price = input("请输入新物品价格：")
            good_num = input("请输入新物品数量：")
            shoppingcar[good_name] = {'price': good_price, 'num': good_num}
            print("修改完成！")

        case "3":
            good_name = input("请输入删除物品名称：")
            if good_name not in shoppingcar:
                print("物品不存在！")
                continue
            else:
                del shoppingcar[good_name]
                print("删除完成！")

        case "4":
            for key in shoppingcar.keys():
                shopping=shoppingcar[key]
                print(f"物品名称：{key} 物品价格：{shopping['price']} 物品数量：{shopping['num']}")

        case "5":
            print("bye~")
            break
        case _:
            print("操作有误！！")

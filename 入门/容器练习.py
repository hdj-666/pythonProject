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
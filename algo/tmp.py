# def func(x:str,y:int)->str:
#     # 要約の出し方「"""」と入力後Enterを押す
#     """商品の価格説明関数

#     Args:
#         x (str): 商品名
#         y (int): 価格

#     Returns:
#         str: 説明文
#     """
#     return f"{x}は{y}円です"

a=8
b=1

scores=[4,1,9,3,a,b]

for x  in scores:
    if x==0:
        print("失格です")
    elif x<5:
        print("追試です")
    else:
        print("合格です")
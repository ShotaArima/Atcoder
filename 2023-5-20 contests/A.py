import math
from decimal import Decimal, ROUND_UP

a,b =list(map(int,input().split()))

ans=a//b
if a%b!=0:
    ans+=1
# print(ans)
rounded_num1 = math.ceil(Decimal(ans).to_integral_value(rounding=ROUND_UP))
print(rounded_num1)

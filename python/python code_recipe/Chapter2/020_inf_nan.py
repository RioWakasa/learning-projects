# 無限大や非数を表したい
'''
Syntax
float('inf') 正の無限大(infinity)
-float('inf') 負の無限大
float('nan') 非数(Not a Number)
'''

x = float('inf')
y = -float('inf')

z1 = x + 100
z2 = x + y
z3 = x / y

print(z1)
print(z2)
print(z3)

'''
inf
nan
nan
'''
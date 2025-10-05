# ブール演算を使いたい
'''
Syntax
not x 否定(xでない)
x and y 論理積(xかつyである)
x or y 論理和(xもしくはyである)
'''

# ブール演算
a = True
b = False

# aかつb
x = a and b
print(x)

# sもしくはb
y = a or b
print(y)

# aではない
z = not a
print(z)

'''
False
True
False
'''

# ブール演算の優先順位
# not > or > andの順で優先度が決まっている
b = True or True and False
print(b)

'''
評価順序の意図がわかりづらいため丸括弧で演算順序を明示するのがおすすめ
b = True or (True and False)
print(b)
'''

'''
True
'''
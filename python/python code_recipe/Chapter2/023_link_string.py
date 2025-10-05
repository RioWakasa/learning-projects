# 文字列を連結したい
'''
Syntax
str型文字列1 + str型文字列2 + ... str型文字列1, str型文字列2, ...を連結
'''

text1 = "abc"
text2 = "def"
text3 = text1 + text2
print(text3)

'''
abcdef
'''

text1 = "abc"
num = 3
text2 = text1 + str(num)
print(text2)

'''
abc3
'''
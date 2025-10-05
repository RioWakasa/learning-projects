# 文字列を扱いたい
'''
Syntax
変数例1 'ABCDEFG' シングルクオートで囲む
変数例2 "ABCDEFG" ダブルクオートで囲む
変数例3 """ABD¥CDEFG""" トリプルクオートで囲む
'''

text1 = 'ABCDEFG'
text2 = "ABCDEFG"
text3 = """
ABCDEFG
HIJKLMN
OPQRSTU
"""

print(text1)
print(text2)
print(text3)

'''
ABCDEFG
ABCDEFG

ABCDEFG
HIJKLMN
OPQRSTU
'''

three = str(3)
# 整数の3から文字列の'3'を生成
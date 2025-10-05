# 文字列をエスケープしたい
'''
Syntax
\エスケープしたい文字
'''

# text = 'I'm pythonista.'
# 実行するとSyntaxError: invalid syntaxが発生
# print(text)

text = 'I\'m pythonista.'
print(text)

'''
I'm pythonista.
'''

'''
代表的なエスケープシーケンス(UNIX系では¥ -> \)
¥改行　¥と改行を無視
¥¥ ¥
¥' 一重引用符(')
¥" 二重引用符(")
¥n 行送り(LF)
¥r 復帰(CR)
¥t タブ(TAB)
'''

text = "aaa\
bbb"
print(text)

'''
aaabbb
'''

text = "aaa\tbbb\tccc\nddd\teee\tfff"
print(text)

'''
aaa   bbb   ccc
ddd   eee   fff
'''
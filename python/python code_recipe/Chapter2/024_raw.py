# raw文字列を使いたい

'''
Syntax
r"文字列" エスケープシーケンスを無効化する
'''

text = r"aaa\nbbb\nccc"
print(text)

'''
aaa\nbbb\nccc
'''

win_path1 = "c:¥¥work¥¥sample"
print(win_path1)
win_path2 = r"c:¥work¥sample"
print(win_path2)

'''
c:¥work¥sample
c:¥work¥sample
'''

# 文字列を囲んだ引用符を文字列中で使用する場合は¥マークでのエスケープが必要
# 文字列末尾に奇数個の¥がある場合、最後の¥が閉じ引用符をエスケープしてしまうためエラーとなる -> 末尾に¥¥を連結して回避
text = r'Beginner\'s Guide'
win_path3 = r'C:¥work' + '¥¥'
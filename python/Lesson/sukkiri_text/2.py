"""
#scores = (70,)
#print(type(scores))

#セットの利用
scores = {70,80,55,80}
list = [70,80,10,70,30,80]
print(scores)
print(set(list)) #setは重複を省く
scores.add(90)
print(scores)

#ディクショナリの中にディクショナリをネスト
matsuda_scores = {'network':60, 'database':80, 'security':50}
asagi_scores = {'network':80, 'database':65, 'security':92}
member_scores = {
  '松田':matsuda_scores,
  '浅木':asagi_scores
}

print(member_scores['松田']['network'])

member_hobbies = {
  '松田':{'SNS', '麻雀', '自転車'},
  '浅木':{'麻雀', '食べ歩き', '数学', '数学', '数学'}
}

common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies)

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B) #和集合
print(A & B) #積集合
print(A - B) #差集合
print(A ^ B) #対称差
"""

"""
def total_scores(subject):
  for i in scores:
    print(i)
    print(scores[i])
    total = sum(scores[i].values())
    scores[name]['合計'] = total
    average = total / len(subject)
    print(f'{name}の合計:{total}\n{name}の平均:{average}')
    x += total
"""

def number_input(s, low, high):
  while True:
    a = input(s)
    try:
      a = int(a)
      if low <= a <= high:
        break
      else:
        print(f'範囲は{low}~{high}です')
    except ValueError:
      print('数値で入力してください')
  return a

x = 0
n = number_input('人数',1,40)

def input_scores(n):
  global x
  scores = {}
  for i in range(n):
    subject = ['国語', '算数', '理科', '社会', '英語']
    name = input('名前')
    scores[name] = {}
    for i in subject:
      score = number_input(f'{i}の点数',0,100)
      scores[name][i] = score
    total = sum(scores[name].values())
    scores[name]['合計'] = total
    average = total / len(subject)
    print(f'{name}の合計:{total}\n{name}の平均:{average}')
    x += total

  return scores

scores = input_scores(n)
#total_scores(scores,subject)
average = x/n
print(f'クラスの合計{x}\nクラスの平均{average}')

a_hobbies = set() #空のセットを作る
b_hobbies = set()
for j in range(5):
  hobby = input('あなたの趣味は？')
  a_hobbies.add(hobby)
for i in range(5):
  hobby = input('あなたの趣味は？')
  b_hobbies.add(hobby)
input('心の準備ができたらエンターキーを押してください')
print(a_hobbies & b_hobbies)
print(a_hobbies | b_hobbies)
n = (len((a_hobbies & b_hobbies)) / len((a_hobbies | b_hobbies)) * 100)
print(f'相性度{n}%')

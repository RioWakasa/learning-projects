Flag = True
a = 1
while Flag:
  if a <= 10:
    print(a)
    a += 1
  else:
    Flag = False

li = list()
for i in range(10):
  li.append(i+1)
print(li)
for i in li:
  if i % 2 == 0:
    print(i,end = " ")

ages = [28, 50, '秘密', 20, 78, 25, 22, 10, '無回答', 33]
samples = list()
for data in ages:
  if not isinstance(data,int): #第１引数が第２引数の型か確認
    continue
  if data< 20 or data >= 30:
    continue
  samples.append(data)
print(samples)

# count = 1
# print('カレーを召し上がれ')
# while True:
#   print(f'{count}皿のカレーを食べました')
#   okawari = input('おかわりはいかがですか？(y/n)>>')
#   if okawari == 'y':
#     count += 1
#   elif okawari == 'n':
#     print('ごちそうさまでした')
#     break
#   else:
#     print('正しく入力できないならカレーでも食ってろ')
#     count += 1

for i in range(10):
  print(10 - i,end = ',')
print('Lift off !')

for i in range(9):
  if i % 2 != 0:
    continue
  print(f'{i+1}の段:',end = "")
  for j in range(9):
    if (i + 1) * (j + 1) >= 50:
      continue
    else:
      print((i + 1) * (j + 1),end = ',')
  print()

temp = [7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]

# for i in temp:
#   print(i)

temp_new = [7.8,9.1,10.2,11.0,12.5,'N/A',14.3,13.8,12.9,12.4]

# for i in temp:
#   print(i)
# for i in temp_new:
#   print(i)

sum, count = 0, 0
for i in temp_new:
  if isinstance(i,float):
    sum += i
    count += 1
  else:
    continue
avg = sum / count
print(f'平均気温{avg}度')

numbers = [1,1]
ratios = list()

while True:
  n = numbers[-1] + numbers[-2]
  m = numbers[-1] / numbers[-2]
  if n <= 1000:
    numbers.append(n)
    ratios.append(m)
  else:
    break

print(numbers)
print(ratios)

for i,j in enumerate(ratios):
  ratios[i] = round(j, 3)

print(ratios)
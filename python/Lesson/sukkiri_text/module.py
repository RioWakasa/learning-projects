# text = input('何を記録しますか？')
# file = open('diary.txt', 'a')
# file.write(text + '\n')
# file.close()

text = input('今日は何をした？ >>')
with open('sample.txt', 'a') as file:
  file.write(text + '\n')

# import math
# print(f'円周率は{math.pi}')
# print(f'小数点以下を切り上げれば{math.floor(math.pi)}です')
# print(f'小数点以下を切り上げれば{math.ceil(math.pi)}です')

# import math as m
# print(f'円周率は{m.pi}です')
# print(f'小数点以下を切り上げれば{m.floor(m.pi)}です')
# print(f'小数点以下を切り上げれば{m.ceil(m.pi)}です')
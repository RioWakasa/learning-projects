import random

#ディーラーの手札と手札の数値を入れるリスト
c_hand,c_scores = [], [] 
#プレイヤー名と所持コインとベット数と合計の手札と手札の数値と手札の合計を入れるリスト
p_name, p_coin , p_bet, p_hand, p_scores, p_sum, w_l = [], [], [], [], [], [], {}
next, name = 'y', 'none'
n = 5
print(f'最大で{n}回までゲーム可能です')
print('1〜4人までプレイできます')
#プレイ人数の確定
Flag = True
while Flag:
  #p_num=プレイヤー数
  p_num = input('何人でプレイしますか？')
  #int型で表せるか確認し1〜4に含まれているか
  if p_num.isdecimal():
    Flag = False
    p_num = int(p_num)
    if p_num <= 0 or p_num > 4:
      print('プレイ可能人数は1〜4人です')
      Flag = True
  else:
    print('入力に誤りがあります')
for i in range(p_num):
  #初期の所持コイン
  p_coin.append(100)
  #名前の確定
  name = input('あなたの名前を入力してください')
  if name in p_name:
    #名前が重複しないか確認
    while name in p_name:
      print('同じ名前のプレイヤーが存在します')
      name = input('あなたの名前を入力してください')
    p_name.append(name)
  else:
    p_name.append(name)
#ゲーム開始
while True:
  #トランプのリスト
  trump = [
  {1:'spade1', 2:'spade2', 3:'spade3', 4:'spade4', 5:'spade5', 6:'spade6', 7:'spade7', 8:'spade8', 9:'spade9', 10:'spade10', 11:'spade11', 12:'spade12', 13:'spade13'},
  {1:'club1', 2:'club2', 3:'club3', 4:'club4', 5:'club5', 6:'club6', 7:'club7', 8:'club8', 9:'club9', 10:'club10', 11:'club11', 12:'club12', 13:'club13'},
  {1:'heart1', 2:'heart2', 3:'heart3', 4:'heart4', 5:'heart5', 6:'heart6', 7:'heart7', 8:'heart8', 9:'heart9', 10:'heart10', 11:'heart11', 12:'heart12', 13:'heart13', },
  {1:'diamond1', 2:'diamond2', 3:'diamond3', 4:'diamond4', 5:'diamond5', 6:'diamond6', 7:'diamond7', 8:'diamond8', 9:'diamond9', 10:'diamond10', 11:'diamond11', 12:'diamond12', 13:'diamond13', }
  ]
  if next == 'y':
    #初期の所持コインの表示
    for i in range(p_num):
      print(f'{p_name[i]}の所持コインは{p_coin[i]}枚です')
    #掛け金を決める
    for i in range(p_num):
      Flag = True
      while Flag:
        bet = input(f'{p_name[i]}さん Place your bet >>')
        #int型で表せるか確認しベット数が所持コイン数内か確認
        if bet.isdecimal():
          Flag = False
          bet = int(bet)
          if bet > p_coin[i]:
            print('所持コインが足りません')
            Flag = True
          elif bet <= 0:
            print('正しい数字を入力してください')
            Flag = True
          else:
            p_bet.append(bet)
        else:
          print('入力に誤りがあります')
      print(f'{p_name[i]}さんは{p_bet[i]}枚ベットしました')
      p_coin[i] -= p_bet[i]
    #初期手札を配る
    for i in range(p_num):
      p = []
      for j in range(2):
      #プレイヤーの手札=p_hand
        mark = trump[random.randint(0,3)]
        num = random.randint(1,len(mark))
        while not (num in mark):
          num = random.randint(1,len(mark))
        player = mark[num]
        delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
        del mark[delete]
        p.append(player)
      p_hand.append(p)
      #コンピューターの手札=c_hand
    for i in range(2):
      mark = trump[random.randint(0,3)]
      num = random.randint(1,len(mark))
      while not(num in mark):
        num = random.randint(1,len(mark))
      computer = mark[num]
      delete = int(computer.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
      del mark[delete]
      c_hand.append(computer)
    #ディーラーの手札と合計の表示
    print(f"ディーラー: ['{c_hand[0]}']")
    for i in range(p_num):
      print(f'{p_name[i]}の手札: {p_hand[i]}')
    for i in c_hand:
      num = int(i.replace('spade','').replace('club','').replace('heart','').replace('diamond','').replace('11','10').replace('12','10').replace('13','10'))
      c_scores.append(num)
    c_sum = sum(c_scores)
    if 1 in c_scores:
      c_sum += 10
      if c_sum > 21:
        c_sum -= 10
    if c_scores == 1:
      print('ディーラーの手札の合計: ' + str(c_scores[0] + 10))
    else:
      print(f'ディーラーの手札の合計: {c_scores[0]}')
    c_scores = []
    #プレイヤーの手札と合計の表示
    for i in p_hand:
      p = []
      scores = []
      for j in i:
        num = int(j.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
        #.replace('11','10').replace('12','10').replace('13','10'))
        scores.append(num)
      p_scores.append(scores)
      p.append(sum(scores))
      p_sum.append(p)
    for i in range(p_num):
      if p_scores[i][0] == p_scores[i][1] and p_coin[i] >= p_bet[i]:
        print('SPLIT CHANCE')
        print('splitは倍のベット数をかけることで手札を2つにすることができます')
        split = input('splitしますか? (y or n)')
        if split == 'y':
          hand = [[p_hand[i][0]],[p_hand[i][1]]]
          p_hand[i] = []
          p_hand[i].append(hand)
          scores = [[p_scores[i][0]],[p_scores[i][1]]]
          p_scores[i] = []
          p_scores[i].append(scores)
        else:
          print('')
      elif p_scores[i][0] == p_scores[i][1] and p_coin[i] < p_bet[i]:
        print('所持コインが足りないためsplitできません')
    for i in range(p_num):
      if 1 in p_scores[i]:
        p_sum[i][0] += 10
      if p_sum[i][0] == 21:
        print(f'{p_name[i]}: BLACKJACK!')
        p_coin[i] += int(p_bet[i] * 1.5)
        w_l[p_name[i]] = 'BLACKJACK'
        p_sum[i] = [0]
      else:
        print(f'{p_name[i]}の合計: {p_sum[i]}')
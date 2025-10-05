import random

#p_name=プレイヤー名,p_coin=所持コイン
p_name, p_coin =[], []
#n=ゲーム数
n = 5
print(f'最大で{n}回までゲーム可能です\n1〜4人までプレイできます')
#プレイ人数の確定
Flag = True
while Flag:
  #p_num=プレイヤー数
  p_num = input('何人でプレイしますか？')
  #int型で表せるか確認
  if p_num.isdecimal():
    Flag = False
    p_num = int(p_num)
    #1~4に含まれるか確認
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
  #名前が重複しないか確認
  if name in p_name:
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
  #p_bet=プレイヤーのベット数,p_hand=手札,p_scores=手札の数値,p_sum=手札の合計,p_split=スプリット数,w_l=勝敗
  p_bet, p_hand, p_scores, p_sum, p_split, w_l = [], [], [], [], [], {}
  #c_hand=ディーラーの手札,c_scores=手札の数値
  c_hand,c_scores = [], [] 
  #初期の所持コインの表示
  for i in range(p_num):
    print(f'{p_name[i]}の所持コインは{p_coin[i]}枚です')
    p_split.append(0)
    #掛け金を決める
    Flag = True
    while Flag:
      bet = input(f'{p_name[i]} Place your bet >>')
      #int型で表せるか確認しベット数が所持コイン数内か確認
      if bet.isdecimal():
        bet = int(bet)
        if bet > p_coin[i]:
          print('所持コインが足りません')
        elif bet <= 0:
          print('正しい数字を入力してください')
        else:
          p_bet.append(bet)
          Flag = False
      else:
        print('入力に誤りがあります')
    print(f'{p_name[i]}は{p_bet[i]}枚ベットしました')
    p_coin[i] -= p_bet[i]
  #初期手札を配る
  for i in range(p_num):
    p = []
    for j in range(2):
      mark = trump[random.randint(0,3)]
      num = random.randint(1,13)
      #同じカードを引かないように処理
      while not (num in mark):
        num = random.randint(1,13)
      player = mark[num]
      #使ったカードの削除
      delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
      del mark[delete]
      p.append(player)
    p_hand.append(p)
  #ディーラーの手札を配る
  for i in range(2):
    mark = trump[random.randint(0,3)]
    num = random.randint(1,13)
    while not(num in mark):
      num = random.randint(1,13)
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
  if c_scores[0] == 1:
    print(f'ディーラーの手札の合計: [{c_scores[0]+10}]')
  else:
    print(f'ディーラーの手札の合計: [{c_scores[0]}]')
  c_scores = []
  #プレイヤーの手札と合計の表示
  for i in p_hand:
    p = []
    scores = []
    for j in i:
      num = int(j.replace('spade','').replace('club','').replace('heart','').replace('diamond','').replace('11','10').replace('12','10').replace('13','10'))
      scores.append(num)
    p_scores.append(scores)
    p.append(sum(scores))
    p_sum.append(p)
  for i in range(p_num):
    if p_scores[i][0] == p_scores[i][1] and p_coin[i] >= p_bet[i]:
      print(f'{p_name[i]}: SPLIT CHANCE')
      print('splitは倍のベット数をかけることで手札を2つにすることができます\nそれぞれの手札に同じベット数がかかっている状態になります') 
      while True:
        split = input(f'{p_hand[i]}をsplitしますか? (y or n)')
        if split == 'y':
          p = []
          scores = []
          p_coin[i] -= p_bet[i]
          for j in range(2):
            mark = trump[random.randint(0,3)]
            num = random.randint(1,13)
            while not (num in mark):
              num = random.randint(1,13)
            player = mark[num]
            delete = player.replace('spade','').replace('club','').replace('heart','').replace('diamond','')
            del mark[int(delete)]
            delete = int(delete.replace('11','10').replace('12','10').replace('13','10'))
            scores.append(delete)
            p.append(player)
          hand = [[p_hand[i][0],p[0]], [p_hand[i][1], p[1]]]
          p_hand[i] = hand
          scores = [[p_scores[i][0], scores[0]],[p_scores[i][1], scores[1]]]
          p_scores[i] = scores
          p = [[sum(scores[0])], [sum(scores[1])]]
          p_sum[i] = p
          print(f'{p_name[i]}の手札: {p_hand[i]}')
          p_split[i] += 1
          if (p_scores[i][0][0] == p_scores[i][0][1] and p_coin[i] >= p_bet[i]): 
            print(f'{p_name[i]}: SPLIT CHANCE')
            while True:
              split = input(f'{p_hand[i][0]}をsplitしますか? (y or n)')
              if split == 'y':
                p = []
                scores = []
                for j in range(2):
                  mark = trump[random.randint(0,3)]
                  num = random.randint(1,13)
                  while not (num in mark):
                    num = random.randint(1,13)
                  player = mark[num]
                  delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
                  del mark[delete]
                  scores.append(delete)
                  p.append(player)
                hand = [[p_hand[i][0][0],p[0]], [p_hand[i][0][1], p[1]]]
                p_hand[i][0] = hand
                scores = [[p_scores[i][0][0], scores[0]],[p_scores[i][0][1], scores[1]]]
                p_scores[i] = scores
                p = [[sum(scores[0])], [sum(scores[1])]]
                p_sum[i] = p
                print(f'{p_name[i]}の手札: {p_hand[i]}')
                p_split[i] += 1
              elif split == 'n':
                print(f'{p_name[i]}の手札: {p_hand[i]}')
                break
              else:
                print('入力に誤りがあります')
              if (p_scores[i][0][0] == p_scores[i][0][1] and p_coin >= p_bet[i]):
                print(f'{p_name[i]}: SPLIT CHANCE')
                while True:
                  split = input('splitしますか? (y or n)')
                  if split == 'y':
                    p = []
                    scores = []
                    for j in range(2):
                      mark = trump[random.randint(0,3)]
                      num = random.randint(1,13)
                      while not (num in mark):
                        num = random.randint(1,13)
                      player = mark[num]
                      delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
                      del mark[delete]
                      scores.append(delete)
                      p.append(player)
                    hand = [[p_hand[i][0],p[0]], [p_hand[i][1], p[1]]]
                    p_hand[i][0] = hand
                    scores = [[p_scores[i][0], scores[0]],[p_scores[i][1], scores[1]]]
                    p_scores[i] = scores
                    p = [[sum(scores[0][0])], [sum(scores[1][0])]]
                    p_sum[i] = p
                    print(f'{p_name[i]}の手札: {p_hand[i]}')
                    p_split[i] += 1
              elif split == 'n':
                print(f'{p_name[i]}の手札: {p_hand[i]}')
                break
              else:
                print('入力に誤りがあります')
          if (p_scores[i][1][0] == p_scores[i][1][1] and p_coin[i] >= p_bet[i]):
            print(f'{p_name[i]}: SPLIT CHANCE')
            split = input(f'{p_hand[i][1]}splitしますか? (y or n)')
            if split == 'y':
              p = []
              scores = []
              for j in range(2):
                mark = trump[random.randint(0,3)]
                num = random.randint(1,13)
                while not (num in mark):
                  num = random.randint(1,13)
                player = mark[num]
                delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
                del mark[delete]
                scores.append(delete)
                p.append(player)
              hand = [[p_hand[i][1][0],p[0]], [p_hand[i][1][1]], p[1]]
              p_hand[i][0] = hand
              scores = [[p_scores[i][1], scores[0]],[p_scores[i][1], scores[1]]]
              p_scores[i] = scores
              p = [[sum(scores[0][0])], [sum(scores[1][0])]]
              p_sum[i] = p
              print(f'{p_name[i]}の手札: {p_hand[i]}')
              p_split[i] += 1
              if (p_scores[i][1][0] == p_scores[i][1][1] and p_coin >= p_bet[i]):
                print(f'{p_name[i]}: SPLIT CHANCE')
                split = input('splitしますか? (y or n)')
                if split == 'y':
                  p = []
                  scores = []
                  for j in range(2):
                    mark = trump[random.randint(0,3)]
                    num = random.randint(1,13)
                    while not (num in mark):
                      num = random.randint(1,13)
                    player = mark[num]
                    delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
                    del mark[delete]
                    scores.append(delete)
                    p.append(player)
                  hand = [[p_hand[i][1],p[0]], [p_hand[i][1], p[1]]]
                  p_hand[i][0] = hand
                  scores = [[p_scores[i][1], scores[0]],[p_scores[i][1], scores[1]]]
                  p_scores[i] = scores
                  p = [[sum(scores[0][0])], [sum(scores[1][0])]]
                  p_sum[i] = p
                  print(f'{p_name[i]}の手札: {p_hand[i]}')
                  p_split[i] += 1
          break
        elif split == 'n':
          print(f'{p_name[i]}の手札: {p_hand[i]}')
          break
        else:
          print('入力に誤りがあります')
    elif p_scores[i][0] == p_scores[i][1] and p_coin[i] < p_bet[i]:
      print(f'{p_name[i]}: 所持コインが足りないためsplitできません')
  for i in range(p_num):
    if p_split[i] == 0:
      if 1 in p_scores[i]:
        p_sum[i][0] += 10
      if p_sum[i][0] == 21:
        print(f'{p_name[i]}: BLACKJACK!')
        p_coin[i] += int(p_bet[i] * 1.5)
        w_l[p_name[i]] = 'BLACKJACK'
        p_sum[i] = [0]
      else:
        print(f'{p_name[i]}の合計: {p_sum[i]}')
    else:
      for j in range(p_split[i] + 1):
        if 1 in p_scores[i][j]:
          p_sum[i][j][0] += 10
        print(f'{p_name[i]}の手札{[j+1]}の合計: {p_sum[i][j]}')
  #プレイヤーが引く
  for i in range(p_num):
    #m=プレイヤーのドロー数
    m = 0
    while True:
      #ブラックジャックか確認
      if p_sum[i] != [0]:
        #初回のドロー
        if p_split[i] == 0:
          print(f'{p_name[i]}の手札: {p_hand[i]}')
          if m == 0:
            h_s = input(f'{p_name[i]}: hit or stand or double? (h or s or d)')
          #2回目以降
          else:
            h_s = input(f'{p_name[i]}: hit or stand? (h or s)')
          #hitの時
          if h_s == 'h':
            mark = trump[random.randint(0,3)]
            num = random.randint(1,13)
            while not (num in mark):
              num = random.randint(1,13)
            player = mark[num]
            delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
            del mark[delete]
            p_hand[i].append(player)
            p = []
            scores = []
            for j in p_hand[i]:
              num = int(j.replace('spade','').replace('club','').replace('heart','').replace('diamond','').replace('11','10').replace('12','10').replace('13','10'))
              scores.append(num)
            p_scores[i] = scores
            p.append(sum(p_scores[i]))
            p_sum[i] = p
            if 1 in p_scores[i]:
              p_sum[i][0] += 10
              if p_sum[i][0] > 21:
                p_sum[i][0] -= 10
            print(f'{p_name[i]}の手札: {p_hand[i]}')
            print(f'{p_name[i]}の合計: {p_sum[i]}')
            m += 1
            if p_sum[i][0] > 21:
              print('BURSTED')
              w_l[p_name[i]] = 'BURSTED'
              p_sum[i] = [0]
              break
            elif p_sum[i][0] == 21:
              break
          elif h_s == 's':
              break
          elif h_s == 'd':
              p_coin[i] -= p_bet[i]
              p_bet[i] = (p_bet[i] * 2)
              mark = trump[random.randint(0,3)]
              num = random.randint(1,13)
              while not (num in mark):
                num = random.randint(1,13)
              player = mark[num]
              delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
              del mark[delete]
              p_hand[i].append(player)
              p = []
              scores = []
              for j in p_hand[i]:
                num = int(j.replace('spade','').replace('club','').replace('heart','').replace('diamond','').replace('11','10').replace('12','10').replace('13','10'))
                scores.append(num)
              p_scores[i] = scores
              p.append(sum(p_scores[i]))
              p_sum[i] = p
              print(f'{p_name[i]}の手札: {p_hand[i]}')
              print(f'{p_name[i]}の合計: {p_sum[i]}')
              if p_sum[i][0] > 21:
                print('BURSTED')
                w_l[p_name[i]] = 'BURSTED'
                p_sum[i] = [0]
              break
          else:
            print('入力が違います')
        else:
          #初回のドロー
          for j in range(p_split[i] + 1):
            m = 0
            print(f'{p_name[i]}の手札{[j+1]}: {p_hand[i][j]}')
            while True:
              if p_sum[i][j] != 21:
                if m == 0:
                  h_s = input(f'{p_name[i]}: hit or stand or double? (h or s or d)')
                #2回目以降
                else:
                  h_s = input(f'{p_name[i]}: hit or stand? (h or s)')
                #hitの時
                if h_s == 'h':
                  mark = trump[random.randint(0,3)]
                  num = random.randint(1,13)
                  while not (num in mark):
                    num = random.randint(1,13)
                  player = mark[num]
                  delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
                  del mark[delete]
                  p_hand[i][j].append(player)
                  p = []
                  scores = []
                  for k in p_hand[i][j]:
                    num = int(k.replace('spade','').replace('club','').replace('heart','').replace('diamond','').replace('11','10').replace('12','10').replace('13','10'))
                    scores.append(num)
                  p_scores[i][j] = scores
                  p.append(sum(p_scores[i][j]))
                  p_sum[i][j] = p
                  if 1 in p_scores[i][j]:
                    p_sum[i][j][0] += 10
                    if p_sum[i][j][0] > 21:
                      p_sum[i][j][0] -= 10
                  print(f'{p_name[i]}の手札: {p_hand[i][j]}')
                  print(f'{p_name[i]}の合計: {p_sum[i][j]}')
                  m += 1
                  if p_sum[i][j][0] > 21:
                    print('BURSTED')
                    w_l[p_name[i]] = 'BURSTED'
                    p_sum[i][j] = [0]
                    break
                  elif p_sum[i][j][0] == 21:
                    break
                elif h_s == 's':
                    break
                elif h_s == 'd':
                    p_coin[i] -= p_bet[i][j][0]
                    p_bet[i][j][0] = (p_bet[i][j][0] * 2)
                    mark = trump[random.randint(0,3)]
                    num = random.randint(1,13)
                    while not (num in mark):
                      num = random.randint(1,13)
                    player = mark[num]
                    delete = int(player.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
                    del mark[delete]
                    p_hand[i][j].append(player)
                    p = []
                    scores = []
                    for k in p_hand[i][j]:
                      num = int(k.replace('spade','').replace('club','').replace('heart','').replace('diamond','').replace('11','10').replace('12','10').replace('13','10'))
                      scores.append(num)
                    p_scores[i][j] = scores
                    p.append(sum(p_scores[i][j]))
                    p_sum[i][j] = p
                    if 1 in p_scores[i][j]:
                      p_sum[i][j][0] += 10
                      if p_sum[i][j][0] > 21:
                        p_sum[i][j][0] -= 10
                    print(f'{p_name[i]}の手札: {p_hand[i][j]}')
                    print(f'{p_name[i]}の合計: {p_sum[i][j]}')
                    if p_sum[i][j][0] > 21:
                      print('BURSTED')
                      w_l[p_name[i]] = 'BURSTED'
                      p_sum[i][j] = [0]
                    break
                else:
                  print('入力が違います')
              else:
                print('合計が21のため引きません')
                break
            break
      else:
        break
      print(p_sum)
  #コンピューターが引く
  if len(w_l) != p_num:
    print(f'ディーラーの手札: {c_hand}')
    print(f'ディーラーの手札の合計: {c_sum}')
    if c_sum <= 16:
      while c_sum <= 16:
        mark = trump[random.randint(0,3)]
        num = random.randint(1,13)
        while not(num in mark):
          num = random.randint(1,13)
        computer = mark[num]
        delete = int(computer.replace('spade','').replace('club','').replace('heart','').replace('diamond',''))
        del mark[delete]
        c_hand.append(computer)
        for i in c_hand:
          num = int(i.replace('spade','').replace('club','').replace('heart','').replace('diamond','').replace('11','10').replace('12','10').replace('13','10'))
          c_scores.append(num)
        c_sum = sum(c_scores)
        if 1 in c_scores:
          c_sum += 10
          if c_sum > 21:
            c_sum -= 10
        print(f'ディーラーの手札: {c_hand}')
        print(f'ディーラーの手札の合計: {c_sum}')
        del c_scores[0:len(c_scores)]
    if c_sum > 21:
      c_sum = 0
    #勝敗の決定
    for i in range(p_num):
      if p_split[i] == 0:
        if 0 < p_sum[i][0] <= 21:
          if c_sum < p_sum[i][0]:
            w_l[p_name[i]] = 'WIN'
            p_coin[i] += (p_bet[i] * 2)
          elif c_sum == p_sum[i]:
            w_l[p_name[i]] = 'DRAW'
            p_coin[i] += p_bet[i]
          else:
            w_l[p_name[i]] = 'LOSE'
      else:
        for j in range(split[i]+1):
          if 0 < p_sum[i][j][0] <= 21:
            if c_sum < p_sum[i][j]:
              w_l[p_name[i]] = 'WIN'
              p_coin[i] += (p_bet[i][j] * 2)
            elif c_sum == p_sum[i]:
              w_l[p_name[i]] = 'DRAW'
              p_coin[i] += p_bet[i][j]
            else:
              w_l[p_name[i]] = 'LOSE'
  Flag = False
  for i in p_name:
    print(f'{i}: {w_l[i]}')
  for i in range(p_num):
    print(f'{p_name[i]}の所持コイン: {p_coin[i]}枚')
    if p_coin[i] <= 0:
      Flag = True
  if Flag:
    print('所持コインが足りません')
    break
  n -= 1
  if n == 0:
    print('No more bet')
    break
  else:
    next = input('continue? (y or n)')
    if not (next == 'y' or next == 'n'):
      while not (next == 'y' or next == 'n'):
        print('入力に誤りがあります')
        next = input('continue? (y or n)')
    if next == 'n':
      for i in range(p_num):
        print(f'{p_name[i]}さんの所持コイン{p_coin[i]}枚')
      break
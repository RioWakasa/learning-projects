import random
from wsgiref.validate import InputWrapper

janken = ["グー","チョキ","パー"]
acchimuite = ["右","左","下","上"]
win, lose = 0, 0
print('ジャンケンとあっち向いてホイをします。\n3点先取です。')
print('ジャンケンはカタカナで入力してください。\nあっち向いてホイは上、下、右、左から入力してください。')
while win < 3 and lose < 3:
  player = input("ジャンケン...")
  computer = random.choice(janken)
  if player == "グー" or player == "チョキ" or player == "パー":
    print("あなた: " + player)
    print("相手: " + computer)
    while player == computer:
      player = input("あいこで...")
      computer = random.choice(janken)
      print("あなた: " + player)
      print("相手: " + computer)
    if player == "グー":
      if computer == "チョキ":
        player = input('あっちむいてホイ')
        computer = random.choice(acchimuite)
        print('あなた: ' + player)
        print('相手: ' + computer)
        if player == computer:
          win += 1
        if win == 0 or win == 1 or win == 2:
          print('{}勝{}敗'.format(win, lose))
        else:
          print('あなたの勝ちです!')
      elif computer == "パー":
        player = input('あっちむいてホイ')
        computer = random.choice(acchimuite)
        print('あなた: ' + player)
        print('相手: ' + computer)
        if player == computer:
          lose += 1
        if win == 0 or win == 1 or win == 2:
          print('{}勝{}敗'.format(win, lose))
          if lose == 3:
            print("何で負けたか明日までに考えといてください")
    elif player == "チョキ":
      if computer == "パー":
        player = input('あっちむいてホイ')
        computer = random.choice(acchimuite)
        print('あなた: ' + player)
        print('相手: ' + computer)
        if player == computer:
          win += 1
        if win == 0 or win == 1 or win == 2:
          print('{}勝{}敗'.format(win, lose))
        else:
          print('あなたの勝ちです!')
      elif computer == "グー":
        player = input('あっちむいてホイ')
        computer = random.choice(acchimuite)
        print('あなた: ' + player)
        print('相手: ' + computer)
        if player == computer:
          lose += 1
        if win == 0 or win == 1 or win == 2:
          print('{}勝{}敗'.format(win, lose))
          if lose == 3:
            print("何で負けたか明日までに考えといてください")
    elif player == "パー":
      if computer == "グー":
        player = input('あっちむいてホイ')
        computer = random.choice(acchimuite)
        print('あなた: ' + player)
        print('相手: ' + computer)
        if player == computer:
          win += 1
        if win == 0 or win == 1 or win == 2:
          print('{}勝{}敗'.format(win, lose))
        else:
          print('あなたの勝ちです!')
      elif computer == "チョキ":
        player = input('あっちむいてホイ')
        computer = random.choice(acchimuite)
        print('あなた: ' + player)
        print('相手: ' + computer)
        if player == computer:
          lose += 1
        if win == 0 or win == 1 or win == 2:
          print('{}勝{}敗'.format(win, lose))
          if lose == 3:
            print("何で負けたか明日までに考えといてください")
  else:
    print("入力に誤りがあります")
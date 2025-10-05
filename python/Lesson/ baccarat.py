from prebaccarat import Baccarat
from player import Player
import math

players = []

#数値の入力チェック
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

#参加人数の決定
def guest():
  p_num = number_input('何人で参加しますか？', 1, 5)
  return p_num

#参加者のインスタンス化
def instance(p_num):
  for i in range(p_num):
    p = Player()
    p.name = i + 1
    p.coin += 100
    players.append(p)

#bet数を決める
def bet(p_num, bet_person):
  for i in range(p_num):
    if players[i].Flag == True:
      while True:
        print('player,banker,引き分け(tie)にかけます\nplayer(2倍),banker(1.95倍),tie(9倍)')
        b = input(f'{players[i].name}: 誰にかけますか？(p or b or t)')
        if b == 'p' or b == 'b' or b == 't':
          break
        else:
          print('入力に誤りがあります')
      print(f'{players[i].name}の所持コインは{players[i].coin}枚です')
      bet = number_input(f'{players[i].name}: Place your bet >>', 1, players[i].coin)
      players[i].bet = bet
      print(f'{players[i].name}は{players[i].bet}枚ベットしました')
      players[i].coin -= players[i].bet
      bet_person.append(b)
  return bet_person

#カードを引く
def draw(pb):
  h = baccara.trump.deal()
  n = baccara.trump.num(h)
  n = change_number(n)
  pb.hand.append(h)
  pb.number.append(n)

#最初の手札を配る(n枚)
def first_draw(n):
  for i in range(n):
    draw(baccara.player)
    draw(baccara.banker)

#数字を変更する(10以上は0にする)
def change_number(n):
  if n >= 10:
    n = 0
  return n

#ゲーム開始時の処理
def game_start(p_num):
  baccara = Baccarat()
  bet_person = bet(p_num, baccara.bet_person)
  baccara.trump.shuffle() #シャッフル
  first_draw(2, baccara)
  return baccara

#手札の合計の下一桁
def score_sum(pb):
  s = str(sum(pb.number))[-1]
  return int(s)

#playerが引くか
def player_check(player_score, banker_score):
  if 0 <= player_score <= 5 or (6 <= player_score <= 7 and 0 <= banker_score <= 5):
    draw(baccara.player)
    player_score = score_sum(baccara.player)
    print('playerが1枚引きました')
  elif 8 <= player_score <= 9 or (6 <= player_score <= 7 and 6 <= banker_score <= 9):
    pass
  else:
    print('error')
  return player_score

#bankerが引くか
def banker_check(player_score,banker_score):
  if 0 <= player_score <= 7:
    for i in range(4):
      if i * 2 <= player_score <= i * 2 + 1 and 0 <= banker_score <= i + 3:
        draw(baccara.banker)
        banker_score = score_sum(baccara.banker)
        print('bankerが1枚引きました')
        break
  elif (player_score == 8 and 0 <= banker_score <= 2) or (player_score == 9 and 0 <= banker_score <= 3):
    draw(baccara.banker)
    banker_score = score_sum(baccara.banker)
    print('bankerが1枚引きました')
  return banker_score

#勝敗の決定
def judge(player_score, banker_score):
  if player_score > banker_score:
    print('player WIN')
    j = 'p'
  elif player_score < banker_score:
    print('banker WIN')
    j = 'b'
  else:
    print('TIE')
    j = 't'
  return j

#掛け金の計算
def calc(p_num, j, bet_person):
  for i in range(p_num):
    if j == 'p' and bet_person[i] == 'p':
      players[i].coin += players[i].bet * 2
    elif j == 'b' and bet_person[i] == 'b':
      players[i].coin += math.ceil(players[i].bet * 1.95)
    elif j == 't' and bet_person[i] == 't':
      players[i].coin += players[i].bet * 9

#ゲームを続けるか
def game_continue(players):
  for i in range(len(players)):
    if players[i].coin >= 1:
      while True:
        c = input('ゲームを続けますか?(y or n)')
        if c == 'y':
          break
        elif c == 'n':
            players[i].Flag = False
            break
        else:
          ('入力に誤りがあります')
    else:
      print(f'{players[i].name}は賭けられるコインがありません')
      players[i].Flag = False

def continue_check(players):
  count = 0
  for i in range(len(players)):
    if players[i].Flag == False:
      count += 1
  return count

p_num = guest()
instance(p_num)
while True:
  baccara = game_start(p_num)
  player_score = score_sum(baccara.player)
  banker_score = score_sum(baccara.banker)
  print(f'プレイヤーの手札{baccara.player.hand}\nバンカーの手札{baccara.banker.hand}')
  player_score = player_check(player_score, banker_score)
  if len(baccara.player.hand) == 3:
    print(f'プレイヤーの手札{baccara.player.hand}')
    banker_score = banker_check(player_score, banker_score)
  print(f'プレイヤーの手札{baccara.player.hand}\nバンカーの手札{baccara.banker.hand}')
  j = judge(player_score, banker_score)
  calc(len(players), j, baccara.bet_person)
  for i in range(p_num):
    if players[i].Flag:
      print(f'{players[i].name}の所持コイン{players[i].coin}')
  game_continue(players)
  count = continue_check(players)
  if count == p_num:
    break
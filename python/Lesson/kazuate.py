import random
from number import Number_input

class Game:
  answer = list()
  prediction = list()
  hit = 0
  ball = 0
  Flag = True
  life = 3
  death = 0
  next_game = False

  def make_answer(self):
    for i in range(4):
      while True:
        num = random.randint(0,9)
        if not (num in self.answer):
          if i != 3:
            self.answer.append(num)
            break
          else:
            self.death = num
            break
  
  # def number_input(self, text, low, high):
  #   while True:
  #     num = input(text)
  #     try:
  #       num = int(num)
  #       if low <= num <= high:
  #         break
  #       else:
  #         print(f'範囲は{low}~{high}です')
  #     except ValueError:
  #       print('数値で入力してください')
  #   return num

  def make_prediction(self):
    print(f'今のライフは{self.life}です。')
    self.life -= 1
    prediction = Number_input('予想数値(3桁)を入力(0~9) >>')
    prediction = str(prediction)
    for i in range(3):
      self.prediction.append(prediction[i])
      self.prediction[i] = int(self.prediction[i])

  def check_number(self):
    count = 0
    for i in self.prediction:
      count += 1
      if self.death == i:
        self.life -= 1
      for j in range(3):
        if i == self.answer[j] and count-1 == j:
          self.hit += 1
          self.life += 1
        elif i == self.answer[j]:
          self.ball += 1
    print(f'{self.hit}ヒット!{self.ball}ボール!')
    if self.hit == 3:
      print('正解です!')
      self.Flag = False
      self.next_game = True
    elif self.life <= 0:
      print(f'ライフがなくなりました。\n正解は{self.answer}でした。')
      self.Flag = False
    else:
      self.hit, self.ball = 0,0
      self.prediction = []
      next = int(input('続けますか? 1:続ける 2:終了 >>'))
      if next == 2:
        print(f'正解は{self.answer}でした。')
        self.Flag = False

  def death_check(self):
    count = 0
    print('デスナンバーを当ててください。\nチャンスは2回です。')
    print('外した場合、デスナンバーが予想より高い(hi)か低い(low)か表示します。')
    while True:
      count += 1
      yosou = int(input('デスナンバーの予想を入力 >>'))
      if yosou == self.death:
        print('おめでとうございます!\nあなたは生き残りました。')
        break
      else:
        if count == 1:
          if yosou > self.death:
            print('low\n残り1回')
          else:
            print('hi\n残り1回')
        else:
          print('GAME OVER')
          print(f'デスナンバーは{self.death}でした。')
          break


  def game_main(self):
    print('数当てゲームを始めます。\nライフがなくなるまでに3桁の数を当ててください!')
    self.make_answer()
    while self.Flag:
      self.make_prediction()
      self.check_number()
    if self.next_game:
      self.death_check()

game = Game()
game.game_main()
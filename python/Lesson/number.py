class Number_input:
  def __init__(self,text):
    while True:
      self.num = input(text)
      try:
        self.num = int(self.num)
        break
      except ValueError:
        print('数値で入力してください')

  def range_check(self, low, high):
    if low <= self.num <= high:
      pass
    else:
      print(f'範囲は{low}~{high}です')

  # def overlap(self):
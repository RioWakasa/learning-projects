class Input:
  def number_input(self, text):
    while True:
      num = input(text)
      try:
        num = int(num)
        break
      except ValueError:
        print('数値で入力してください')
    return num

  def range_check(self, text, low, high):
    while True:
      num = self.number_input(text)
      if low <= num <= high:
        break
      else:
        print(f'範囲は{low}~{high}です')
    return num

  def yes_no(self, text):
    inp = input(text)
    print()
    if not (inp == 'y' or inp == 'n'):
      while not (inp == 'y' or inp == 'n'):
        print('入力に誤りがあります')
        inp = input(text)
    if inp == 'y':
      return True
    else:
      return False

  def name_input(self, text, p_num, names):
    for i in range(p_num):
      name = input(text)
      if name in name:
        while name in names:
          print(f'{name}はすでに存在しています')
          name = input(text)
      names.append(name)
    print()
    return names
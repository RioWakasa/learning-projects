# モジュールをインポートしたい
'''
Syntax
import モジュール as 別名 -> モジュールをインポートする
from モジュール import インポート対称 as 別名 -> モジュールの中で特定の属性のみimportする
'''
import math
print(math.pi)

from math import pi
print(pi)

import math as m
print(m.pi)
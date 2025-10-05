class Status:
  start_status = {'勇者':{'HP':10,'MP':10,'ATK':10,'DEF':10,'INT':10,'RES':10,'AGI':10},
                  '剣士':{'HP':12,'MP':5,'ATK':15,'DEF':12,'INT':6,'RES':9,'AGI':8},
                  'アーチャー':{'HP':7,'MP':5,'ATK':12,'DEF':8,'INT':7,'RES':8,'AGI':11},
                  '魔法使い':{'HP':8,'MP':15,'ATK':6,'DEF':8,'INT':14,'RES':12,'AGI':8},
                  '僧侶':{'HP':8,'MP':15,'ATK':6,'DEF':10,'INT':11,'RES':10,'AGI':7},
                  '盗賊':{'HP':9,'MP':9,'ATK':11,'DEF':9,'INT':9,'RES':9,'AGI':13}
  }
  def __init__(self, job):
    self.status = self.start_status[job]
  #def lvup(self):

class Hero:
  gold = 100
  def __init__(self,name,lv,job):
    self.name = name
    self.lv = lv
    self.job = job
    self.status = Status(job)

a = Hero('a', 1, '勇者')
print(a.status.status)
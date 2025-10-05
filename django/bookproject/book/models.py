from secrets import choice
from sre_parse import CATEGORIES
from django.db import models

class Book(models.Model):
  CATEGORY = (('life','生活'),('business','ビジネス'),('other','その他'))
  title = models.CharField(max_length=200)
  text = models.TextField(max_length=100)
  category = models.CharField(max_length=100,choices=CATEGORY)

  def __str__(self):
    return self.title
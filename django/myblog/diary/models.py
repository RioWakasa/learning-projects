from django.db import models

class Diary(models.Model):
  topic = models.CharField(max_length=100)
  wheather = models.CharField(max_length=100, null=True)

  def __str__(self):
      return self.topic
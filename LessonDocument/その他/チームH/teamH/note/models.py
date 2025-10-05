from django.db import models

class Subject(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
      return self.name

class Document(models.Model):
  title = models.CharField(max_length=100)
  url = models.CharField(max_length=100)
  subject_id = models.IntegerField()

  def __str__(self):
      return self.title
from django.db import models
from django.urls import reverse

class Category(models.Model):
  name = models.CharField(max_length=255)
  author = models.ForeignKey( #外部キー 別テーブルを参照
    'auth.User', # Djangoの用意しているUserテーブルを参照
    on_delete=models.CASCADE,
  )
  created_at = models.DateTimeField(auto_now_add=True) #新規作成した時間を自動で取得
  updated_at = models.DateTimeField(auto_now=True) #更新した時間を自動で取得

  def __str__(self):
    return self.name

class Shop(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )
  category = models.ForeignKey( #Categoryテーブルのidを参照している
    Category,
    on_delete=models.PROTECT,
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('lunchmap:detail', kwargs={'pk': self.pk})
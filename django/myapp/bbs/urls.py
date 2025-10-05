from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
  path('', views.index, name='index'), # 一覧表示
  path('<int:id>', views.detail, name='detail'), # 詳細表示
  path('new', views.new, name='new'), # 登録ページの表示
  path('<int:id>/edit', views.edit, name='edit'), # 編集ページの表示
  path('<int:id>/update', views.update, name='update'), # 更新ページの表示
  path('create', views.create, name='create'), # 新規作成ページの表示
  path('<int:id>/delete', views.delete, name='delete'), # 削除
]
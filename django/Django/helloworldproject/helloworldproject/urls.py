from django.contrib import admin
from django.urls import path
from .views import helloworldfunc

urlpatterns = [
    path('hello/', admin.site.urls),
    path('helloworldurl/', helloworldfunc)
]
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postuser/', views.postuser, name='postuser'),
]
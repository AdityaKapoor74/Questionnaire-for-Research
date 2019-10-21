from django.urls import path
from django.conf.urls import include,url
from .import views

urlpatterns = [
    path('', views.register, name='register'),
    path("registered/", views.register_done, name='register_done'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('sample/',views.sample, name='sample'),
    path('<int:question_id>/choice/', views.select_option, name='select_option'),
]
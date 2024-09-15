from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainHome, name='mainHome'),
    path('formvalid/', views.formvalid, name='formvalid'),
    path('login/', views.Loginn, name='Loginn'),
    path('homepage/', views.HomePage, name='HomePage'),
    path('logout/', views.Logout, name='Logout'),
    path('addpost/', views.AddPost, name='AddPost'),
    path('addpost/', views.AddPost, name='AddPost'),
    path('deletepost/', views.DeletePost, name='DeletePost'),
    path('post/<int:id>', views.Post, name='Post')
]
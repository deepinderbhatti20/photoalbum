from django.urls import path
from photos import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('addpost/', views.addpost, name='addpost'),
    path('photo/<str:pk>/', views.viewphoto, name='photo'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]

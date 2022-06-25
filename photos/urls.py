from ctypes import alignment
from django.urls import path
from photos import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('addpost/', views.addpost, name='addpost'),
    path('photo/<str:pk>/', views.viewphoto, name='photo'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='reset_emailsent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='reset_passworddone.html'), name='password_reset_complete'),
]

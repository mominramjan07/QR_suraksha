from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.create_profile, name='create_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('emergency/<int:id>/', views.emergency, name='emergency'),
    path("about/", views.about, name="about"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
]
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name = 'home'),
	path('login/', views.view_login, name = 'login'),
	path('logout/', views.view_logout, name = 'logout'),
	path('sign_up/', views.sign_up, name = 'sign_up'),
]
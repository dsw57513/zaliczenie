from django.contrib import admin
from django.urls import path, include
from . import views
#from.views import login_view
app_name = "users"
urlpatterns = [
    path('',views.login_view, name='login'),
    path('logout/', views.logout_view, name = 'logout')
]

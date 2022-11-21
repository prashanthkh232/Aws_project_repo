from awsapp import views
from django.urls import path


urlpatterns = [
    path('login/',views.index,name='login'),
    path('register/',views.regist,name='register'),
    path('',views.home,name='home'),
    path('myaccount/',views.profile,name='profile'),
    path('logout/',views.log_out,name='logout'),
]

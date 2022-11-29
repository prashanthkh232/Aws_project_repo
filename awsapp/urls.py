from awsapp import views
from django.urls import path


urlpatterns = [
    path('login/',views.index,name='login'),
    path('regdisp/',views.regdisp,name='regdisp'),
    path('regdisp/register/',views.regist,name='register'),
    path('',views.home,name='home'),
    path('myaccount/',views.profile,name='profile'),
    path('logout/',views.log_out,name='logout'),
    path('regdisp/register/verifyotp/',views.verifyotp,name='verifyotp'),
    path('regdisp/register/verifyotp/userRegister/',views.userRegister,name='userRegister'),
]

from django.urls import path
from App_Login.views import sign_up, login_page, logout_user, profile, user_change,pass_change, add_profile_pic, change_pro_pic


app_name ='App_Login'

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('change-profile/', user_change, name='user_change'),
    path('password/', pass_change, name='pass_change'),
    path('ad-pro-pic/', add_profile_pic, name='add_profile_pic'),
    path('change-picture/', change_pro_pic, name='change_pro_pic'),
]




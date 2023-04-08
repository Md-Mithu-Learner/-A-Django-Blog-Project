from django.urls import path
from App_Blog.views import blog_list


app_name ='App_Blog'

urlpatterns = [
    path('', blog_list, name='blog_list')


]

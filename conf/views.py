from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


def index(request, *args, **kwargs):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
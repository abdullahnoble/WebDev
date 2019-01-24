from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from mysite import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^', include('mysite.urls')),

]
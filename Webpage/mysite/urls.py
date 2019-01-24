from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from . import views as core_views

app_name = 'mysite'

urlpatterns = [

    url(r'^login/$', auth_views.login, {'template_name': 'mysite/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^info/(?P<pk>[0-9]+)/$', core_views.AddProfile, name='add_profile'),

]
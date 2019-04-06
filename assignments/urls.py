from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'skillMatch'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
]
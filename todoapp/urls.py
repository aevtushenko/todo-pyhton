from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user/register/$', views.registeruser, name='registeruser'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^user/login/$', views.loginuser, name='login'),
    url(r'^task/create/$', views.createtask, name='createtask'),
    url(r'^task/delete/$', views.deletetask, name='deletetask'),
    url(r'^task/complete/$', views.completetask, name='completetask')
 #   url(r'^your-name/', views.name, name='get_name')
]
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from arc import views as core_views

urlpatterns= [
              path('accueil', views.index),
              url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
              url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
              #url(r'^$', views.home, name='home'),


              url(r'^reservation$', views.reservation, name='reservation'),


              url(r'^$', views.home, name='home'),
              #url(r'^$', views.res, name='res'),
              url(r'^signup/$', core_views.signup, name='signup'),
              url(r'^book/$', core_views.book, name='book'),
              url(r'^logement/$', core_views.logement, name='logement'),
              url(r'^vehicule/$', core_views.voiture, name='vehicule'),
              url(r'^service/$', core_views.service, name='service'),
              #url(r'^showv/(?P<id>[0-9]+)$', views.showv, name='showv'),
              #url(r'^showv/(?P<id>[0-9]+)$', views.showv, name='showv'),
              #url(r'^posts/(?P<id>[0-9]+)$', views.showv, name='showv'),
              url(r'^admin/', admin.site.urls, name= 'admin'),
              url(r'^home$', core_views.home, name='home'),
              url(r'^res/$', core_views.res, name='res'),






              url(r'^log/$', views.log, name='log'),
              url(r'^voit/$', views.voit, name='voit'),
              url(r'^serv/$', views.serv, name='serv'),
              ]
# Create your tests here.

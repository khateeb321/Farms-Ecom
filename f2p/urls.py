from django.conf.urls import url
from . import views

app_name='f2p'
urlpatterns = [

    url(r'^$', views.main, name='main'),
    url(r'^f$', views.fruits, name='fruits'),
    url(r'^c$', views.indexCity, name='indexCity'),
    url(r'^a$', views.indexArea, name='indexArea'),
    url(r'^btn$', views.btn, name='btn'),
    url(r'^conf$', views.btnConfirmOrder, name='btnConfirmOrder'),

]

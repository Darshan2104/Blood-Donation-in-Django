from django.urls import path
from . import views
urlpatterns = [

    path('', views.show, name="show"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('registration', views.registration, name="registration"),

    path('alldoner', views.alldoner, name="alldoner"),
    path('allreq', views.allreq, name="allreq"),
    path('allbb', views.allbb, name="allbb"),
    path('allhospital', views.allhospital, name="allhospital"),
    # find tab
    path('finddoner', views.finddoner, name="finddoner"),
    path('findbloodbank', views.findbloodbank, name="findbloodbank"),
    path('findhp', views.findhp, name="findhp"),
    # about tab
    path('mail', views.mail, name='mail'),
    path('look', views.look, name='look'),
    # for fillup forms
    path('donate', views.donate, name="donate"),
    path('req', views.req, name='req'),
    path('bbank', views.bbank, name='bbank'),
    path('hp', views.hp, name='hp'),

]

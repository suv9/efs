from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    #url(r'^customer/(?P<pk>\d+)/delete/$', views.customer_delete, name='customer_delete'),
    url(r'^customer/(?P<pk>\d+)/portfolio/$', views.portfolio, name='portfolio'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    #url(r'^stock/(?P<pk>\d+)/delete/$', views.stock_delete, name='stock_delete'),
    #url(r'^stock/(?P<pk>\d+)/edit/$', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    #url(r'^stock/create/$', views.stock_new, name='stock_new'),
    url(r'^investment/$', views.investment_list, name='investment_list'),
    url(r'^investment/(?P<pk>\d+)/delete/$', views.investment_delete, name='investment_delete'),
    url(r'^investment/(?P<pk>\d+)/edit/$', views.investment_edit, name='investment_edit'),
    url(r'^investment/(?P<pk>\d+)/add/$', views.investment_add, name='investment_add'),
    url(r'^investment/create/$', views.investment_new, name='investment_new'),
]

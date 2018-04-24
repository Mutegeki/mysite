from django.conf.urls import url
from mycar import views

app_name = 'mycar'

urlpatterns = [
    url(r'^$', views.car_list, name='list'),
    url(r'^$', views.service, name='services'),
    url(r'^$', views.repair, name='repair'),
    url(r'^$', views.showcar_list, name='show'),
    url(r'^(?P<reg_no>[\w-]+)/$', views.car_detail, name='details'),
    url(r'^$', views.driver, name='drivers'),
]

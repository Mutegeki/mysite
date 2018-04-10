from django.conf.urls import url
from mycar import views

app_name = 'mycar'

urlpatterns = [
    url(r'^$', views.car_list, name="list"),
    url(r'^$', views.service),
    url(r'^$', views.showcar_list),
    url(r'^(?P<reg_no>[\w-]+)/$', views.car_detail, name='details'),
    #url(r'^car_detail/(\w+)/$', views.car_detail, name='cardetail'),
    #url(r'^$', views.car_detail),
    url(r'^$', views.driver),
]

from django.conf.urls import url
from mycar import views

urlpatterns = [
    url(r'^$', views.car_list),
    url(r'^$', views.service),
    url(r'^$', views.showcar_list),
    url(r'^$', views.driver),
]

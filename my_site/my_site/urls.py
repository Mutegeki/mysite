from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from. import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
import mycar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^car/', include('mycar.urls')),
    url(r'^getdata/',include('mycar.urls')),
    url(r'^showcar_list/', mycar.views.showcar_list),
   	url(r'^driver/', mycar.views.driver),

    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
]

urlpatterns+= staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
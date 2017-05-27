from django.conf.urls import url, include
from django.contrib import admin

from QuP.views import home

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/', include('registration.urls')),
]

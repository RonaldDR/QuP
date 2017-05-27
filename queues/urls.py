from django.conf.urls import url

from .views import window1enqueue, window2enqueue, window3enqueue, window4enqueue, window5enqueue

urlpatterns = [
	url(r'^window1enqueue/$', window1enqueue, name='window1enqueue'),
	url(r'^window2enqueue/$', window2enqueue, name='window2enqueue'),
	url(r'^window3enqueue/$', window3enqueue, name='window3enqueue'),
	url(r'^window4enqueue/$', window4enqueue, name='window4enqueue'),
	url(r'^window5enqueue/$', window5enqueue, name='window5enqueue'),
]
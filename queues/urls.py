from django.conf.urls import url

from .views import window1enqueue, window2enqueue, window3enqueue, window4enqueue, window5enqueue
from .views import window1dequeue, window2dequeue, window3dequeue, window4dequeue, window5dequeue

urlpatterns = [
	url(r'^window1enqueue/$', window1enqueue, name='window1enqueue'),
	url(r'^window2enqueue/$', window2enqueue, name='window2enqueue'),
	url(r'^window3enqueue/$', window3enqueue, name='window3enqueue'),
	url(r'^window4enqueue/$', window4enqueue, name='window4enqueue'),
	url(r'^window5enqueue/$', window5enqueue, name='window5enqueue'),

	url(r'^window1dequeue/$', window1dequeue, name='window1dequeue'),
	url(r'^window2dequeue/$', window2dequeue, name='window2dequeue'),
	url(r'^window3dequeue/$', window3dequeue, name='window3dequeue'),
	url(r'^window4dequeue/$', window4dequeue, name='window4dequeue'),
	url(r'^window5dequeue/$', window5dequeue, name='window5dequeue'),
]
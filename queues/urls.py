from django.conf.urls import url

from .views import window1enqueue, window2enqueue, window3enqueue, window4enqueue, window5enqueue
from .views import window1dequeue, window2dequeue, window3dequeue, window4dequeue, window5dequeue
from .views import window1pop, window2pop, window3pop, window4pop, window5pop

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

	url(r'^window1pop/$', window1pop, name='window1pop'),
	url(r'^window2pop/$', window2pop, name='window2pop'),
	url(r'^window3pop/$', window3pop, name='window3pop'),
	url(r'^window4pop/$', window4pop, name='window4pop'),
	url(r'^window5pop/$', window5pop, name='window5pop'),
]
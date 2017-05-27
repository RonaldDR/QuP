from django.conf.urls import url

from .views import enqueue

urlpatterns = [
	url(r'^enqueue/$', enqueue, name='enqueue'),
]
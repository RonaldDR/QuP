from django.conf.urls import url

from .views import sign_up, sign_in, sign_out

urlpatterns = [
	url(r'^sign-up/$', sign_up, name='sign_up'),
    url(r'^sign-in/$', sign_in, name='sign_in'),
    url(r'^sign-out/$', sign_out, name='sign_out'),
]

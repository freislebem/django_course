from django.conf.urls import url
from blog import views

urlpatterns = [

	url(r'^$', views.home),
	url(r'^/megasena', views.megasena)
]
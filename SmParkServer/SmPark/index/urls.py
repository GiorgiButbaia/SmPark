from django.conf.urls import url, include
from . import views
#TODO fill in handlers/pages
urlpatterns = [
    url(r'^$', views.index, name="index") #Index page
]

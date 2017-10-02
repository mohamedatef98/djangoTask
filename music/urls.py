from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name = 'index'),
    url(r'^register/$',views.UserFormView.as_view(),name = 'register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() ,name ='detail'),
    url(r'^album/add/$',views.CreateAlbum.as_view(),name="addAlbum"),
    url(r'^album/(?P<pk>[0-9]+)/$',views.UpdateAlbum.as_view(),name="updateAlbum"),
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.DeleteAlbum.as_view(),name="deleteAlbum"),

]
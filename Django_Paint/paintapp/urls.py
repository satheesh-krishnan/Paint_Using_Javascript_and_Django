from django.conf.urls import url

from paintapp import views

urlpatterns=[
             url(r'^post/$', views.post),
             url(r'^new/$',views.new),
             url(r'^gett/$',views.gett),
             url(r'^pop/$',views.pop),
             url(r'^gtt/$',views.gtt),
            ]

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.photo_category,name='photoCategory'),
    url('^travel/$',views.travel,name='travel'),
    url('^party/$',views.travel,name='party'),
    url('^activity/$',views.travel,name='activity'),
    url('^school/$',views.travel,name='school')
]
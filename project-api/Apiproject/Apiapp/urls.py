from django.contrib import admin
from django.urls import path,include 
from Apiapp import views 
from rest_framework import routers
from Apiapp.serializers import Userserializer

from Apiapp.views import UserViewSet

router= routers.DefaultRouter()
router.register(r'list' ,UserViewSet)







urlpatterns = [
    path("loginup/", views.home ,name="login"),#login page
    path("signup/" , views.signup ,name="signup"),
    path("register/" , views.register_page, name="register"),# registration page
    path("create_task/", views.create_task, name="create_task"),
    path("post_data/", views.postdata, name="post"),#show all api data
    path("delete/<int:id>/" , views.delete_data , name="delete"),# delete tthe user data
    path("<int:id>/", views.update_data , name="update"),
    path("router/", include(router.urls)), #router/list/ leads to  api page
    path("page/", views.page ,name="page" ),
    path("service/" , views.services , name="service"),
    path("parse/" , views.pagination , name="page"),# url to the main page
    path("create/" , views.create , name="create"),# create user data
    path("filter/" , views.Filter ,name="filter")# filter user data
]

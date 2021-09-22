from django.conf.urls import url
from django.urls import path
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/', views.V1View.as_view()),
    path('dummy_api/v1/', views.DummyView.as_view()),

]
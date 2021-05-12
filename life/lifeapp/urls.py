from django.urls import path,include
from lifeapp import views

urlpatterns=[
path('life',views.life, name='life')]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('hello/', views.HelloWorldView.as_view(), name='hello'),
    path('teams/', include('teams.urls')),
    path('admin/', admin.site.urls),
]

"""hudarubayaw_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from world import views as w_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', w_app.home, name="home"),
    path('index/<username>/', w_app.index, name="index"),
    path('changePassword/<username>/', w_app.changePassword, name="changePassword"),
    path('logOut', w_app.logOut, name="logOut"),
    path('map/<username>/', w_app.map, name="map"),
    path('updateDetails/<username>/', w_app.updateDetails, name="updateDetails"),
    path('login', w_app.login, name="login"),
    path('updateInfo/<username>/', w_app.updateInfo, name="updateInfo"),
    path('signup', w_app.signup, name="signup")
]

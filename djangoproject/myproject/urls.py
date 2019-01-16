"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import myapp.views # 이 안에 있는 함수 쓰기위해 import

urlpatterns = [
    path('admin/', admin.site.urls), 
    # 새로운 url 추가해주면 됨
    path('', myapp.views.home, name="home"), 
    # ''이런 조건일 때 home 호출하고, 이 path의 경로이름은 home이다.
    # name은 함수이름과 동일하게 하는 것이 원칙
    # 비어있으면 default로 실행되는 홈페이지라고 생각하면 됨~
]

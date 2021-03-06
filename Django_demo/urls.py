"""Django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from views import views
from books import views as book_views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hello/$', views.hello),
    url(r'^date/', views.date),
    url(r'add/$', views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
    url(r'^db/$', book_views.create_db),
]

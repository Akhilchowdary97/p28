"""p28 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_topic/',views.create_topic,name="add_topic"),
    path('add_webpage/',views.create_webpage,name="add_webpage"),
    path('display_topic/',views.display_topics,name="display_topic"),
    path('display_topic/<id>',views.display_topic,name="display_topic"),
    path('display_webpage/',views.display_webpages,name="display_webpage"),
    path('display_webpage/<id>',views.display_webpage,name="display_webpage"),
    path('add_access/',views.create_access,name="add_access"),
    path('display_access/',views.display_access1,name='display_access'),
    path('display_access/<id>',views.display_access,name='display_access'),
    path('search/',views.search,name="search"),
]


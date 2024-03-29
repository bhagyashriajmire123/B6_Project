"""Library URL Configuration

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
from unicodedata import name


from django.contrib import admin
from django.urls import path, re_path, include


from Book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),              # this is url
    path("show_all_book/",views.show_all_book, name="show_all_book"),
    path('Edit_Data /<int:id>/',views.Edit_Data, name='Edit_Data'),
    path(' delete /<int:id>/',views.delete, name= 'delete'),
    
]



urlpatterns += [
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),
]

urlpatterns +=[
    path('__debug__/', include('debug_toolbar.urls'))

]

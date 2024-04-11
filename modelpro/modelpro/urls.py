"""
URL configuration for modelpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('add/',views.add_data,name="add"),
    path('delete/<str:email>',views.delete_data,name="delete"),
    path('update/<str:email>',views.update_data,name="update"),
    path('search/',views.search_data,name="search"),
    path('search_male/',views.search_male,name="search_male"),
    path('searchfemale/',views.search_female,name="search_female"),
    path('show/',views.show_all_data,name="show"),
    # path('search_manager/',views.search_manager,name="search_manager"),
    # path('search_designer/',views.search_designer,name="search_designer"),
    # path('search_administration/',views.search_administration,name="search_administration"),
    # path('search_system_administration/',views.search_system_administration,name="search_system_administration"),
    # path('search_application_developer/',views.search_application_developer,name="search_application_developer"),
    # path('search_security_administration/',views.search_security_administration,name="search_security_administration"),
    # path('search_database_administration/',views.search_database_administration,name="search_database_administration"),
    # path('search_web_developer/',views.search_web_developer,name="search_web_developer"),
    # path('search_helpdesk_supporter/',views.search_helpdesk_supporter,name="search_helpdesk_supporter"),
    # path('search_technical_supporter/',views.search_technical_supporter,name="search_technical_supporter"),
    path('search_dept',views.search_dept,name="search_dept"),
    path('filter_salary',views.filter_salary,name='filter_salary'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    

"""objectionApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from objections.views import (
    administrative_tasks, serviceprovider_list, home_page, serviceprovider_detail, serviceprovider_update, 
    serviceprovider_create, agent_list, agent_detail, agent_create
    )

urlpatterns = [
    path('admin/', admin.site.urls),    

    path('', home_page, name = 'home-page'),

    path('administrative-tasks/', administrative_tasks, name='administrative-tasks'), 

    path('administrative-tasks/service-provider/', serviceprovider_list.as_view(), name = 'service-provider'),
    path('administrative-tasks/service-provider/<int:pk>/', serviceprovider_detail.as_view(), name = 'serviceprovider-detail'),
    path('administrative-tasks/service-provider/<int:pk>/update/', serviceprovider_update.as_view(), name = 'serviceprovider-update'),
    #path('administrative-tasks/service-provider/<int:pk>/delete/', serviceprovider_delete.as_view(), name='serviceprovider-delete'),
    path('administrative-tasks/service-provider/create/', serviceprovider_create.as_view(), name='serviceprovider-create'), 

    path('administrative-tasks/agent/', agent_list.as_view(), name = 'agent-home'),
    path('administrative-tasks/agent/<int:pk>/', agent_detail.as_view(), name = 'agent-detail'),
    #path('administrative-tasks/agent/<int:pk>/update/', agent_update.as_view(), name = 'agent-update'),
    #path('administrative-tasks/agent/<int:pk>/delete/', agent_delete.as_view(), name='agent-delete'),
    path('administrative-tasks/agent/create/', agent_create.as_view(), name='agent-create'),     
]

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
    serviceprovider_create, agent_list, agent_detail, agent_create, language_list, language_detail, language_create, language_update,
    statusnote_list, statusnote_detail, statusnote_create, statusnote_update
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

    path('administrative-tasks/language/', language_list.as_view(), name = 'language-list'),
    path('administrative-tasks/language/<int:pk>/', language_detail.as_view(), name = 'language-detail'),
    path('administrative-tasks/language/<int:pk>/update/', language_update.as_view(), name = 'language-update'),
    path('administrative-tasks/language/create/', language_create.as_view(), name='language-create'),        

    path('administrative-tasks/statusnote/', statusnote_list.as_view(), name = 'statusnote-list'),
    path('administrative-tasks/statusnote/<int:pk>/', statusnote_detail.as_view(), name = 'statusnote-detail'),
    path('administrative-tasks/statusnote/<int:pk>/update/', statusnote_update.as_view(), name = 'statusnote-update'),
    path('administrative-tasks/statusnote/create/', statusnote_create.as_view(), name='statusnote-create'),       
]

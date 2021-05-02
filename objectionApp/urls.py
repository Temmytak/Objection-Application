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
    administrative_tasks, home_page,
    serviceprovider_list, serviceprovider_detail, serviceprovider_update, serviceprovider_create, 
    agent_list, agent_detail, agent_create, 
    language_list, language_detail, language_create, language_update,
    statusnote_list, statusnote_detail, statusnote_create, statusnote_update,
    refcode_list, refcode_detail, refcode_create, refcode_update,
    objectionstatus_list, objectionstatus_detail, objectionstatus_create, objectionstatus_update,
    objectionassessment_list, objectionassessment_detail, objectionassessment_create, objectionassessment_update,
    closinglevel_list, closinglevel_detail, closinglevel_create, closinglevel_update,
    cctsassistance_list, cctsassistance_detail, cctsassistance_create, cctsassistance_update,
    customerassistance_list, customerassistance_detail, customerassistance_create, customerassistance_update
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

    path('administrative-tasks/referencedcode/', refcode_list.as_view(), name = 'refcode-list'),
    path('administrative-tasks/referencedcode/<int:pk>/', refcode_detail.as_view(), name = 'refcode-detail'),
    path('administrative-tasks/referencedcode/<int:pk>/update/', refcode_update.as_view(), name = 'refcode-update'),
    path('administrative-tasks/referencedcode/create/', refcode_create.as_view(), name='refcode-create'),   

    path('administrative-tasks/objectionstatus/', objectionstatus_list.as_view(), name = 'objectionstatus-list'),
    path('administrative-tasks/objectionstatus/<int:pk>/', objectionstatus_detail.as_view(), name = 'objectionstatus-detail'),
    path('administrative-tasks/objectionstatus/<int:pk>/update/', objectionstatus_update.as_view(), name = 'objectionstatus-update'),
    path('administrative-tasks/objectionstatus/create/', objectionstatus_create.as_view(), name='objectionstatus-create'),    

    path('administrative-tasks/objectionassessment/', objectionassessment_list.as_view(), name = 'objectionassessment-list'),
    path('administrative-tasks/objectionassessment/<int:pk>/', objectionassessment_detail.as_view(), name = 'objectionassessment-detail'),
    path('administrative-tasks/objectionassessment/<int:pk>/update/', objectionassessment_update.as_view(), name = 'objectionassessment-update'),
    path('administrative-tasks/objectionassessment/create/', objectionassessment_create.as_view(), name='objectionassessment-create'), 

    path('administrative-tasks/closinglevel/', closinglevel_list.as_view(), name = 'closinglevel-list'),
    path('administrative-tasks/closinglevel/<int:pk>/', closinglevel_detail.as_view(), name = 'closinglevel-detail'),
    path('administrative-tasks/closinglevel/<int:pk>/update/', closinglevel_update.as_view(), name = 'closinglevel-update'),
    path('administrative-tasks/closinglevel/create/', closinglevel_create.as_view(), name='closinglevel-create'),  

    path('administrative-tasks/cctsassistance/', cctsassistance_list.as_view(), name = 'cctsassistance-list'),
    path('administrative-tasks/cctsassistance/<int:pk>/', cctsassistance_detail.as_view(), name = 'cctsassistance-detail'),
    path('administrative-tasks/cctsassistance/<int:pk>/update/', cctsassistance_update.as_view(), name = 'cctsassistance-update'),
    path('administrative-tasks/cctsassistance/create/', cctsassistance_create.as_view(), name='cctsassistance-create'),     

    path('administrative-tasks/customerassistance/', customerassistance_list.as_view(), name = 'customerassistance-list'),
    path('administrative-tasks/customerassistance/<int:pk>/', customerassistance_detail.as_view(), name = 'customerassistance-detail'),
    path('administrative-tasks/customerassistance/<int:pk>/update/', customerassistance_update.as_view(), name = 'customerassistance-update'),
    path('administrative-tasks/customerassistance/create/', customerassistance_create.as_view(), name='customerassistance-create'),                 
]

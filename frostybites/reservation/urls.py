from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('services/', views.services_list_admin, name='services_list_admin'),
    path('services/add_service/', views.add_service, name='add_service'),
    path('services/update_service/<int:id>', views.update_service, name='update_service'),
    path('customers/', views.customers, name='customers'),
    path('home', views.services_list, name='services_list'),   
    path('services/delete/<int:id>/', views.delete_service, name='delete_service'),
   
 
]


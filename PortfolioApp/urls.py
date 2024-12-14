from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('project/<int:project_id>/', views.project_detail, name='project'),
    
]
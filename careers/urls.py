from django.urls import path
from . import views

app_name = 'careers'

urlpatterns = [
    path('', views.careers_list, name='list'),
    path('<slug:slug>/', views.job_detail, name='detail'),
    path('<slug:slug>/apply/', views.apply_job, name='apply'),
]

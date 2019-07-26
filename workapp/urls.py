from django.urls import path

from . import views

urlpatterns = [
    path('', views.WorkersListView.as_view(), name='home'),
    path('worker/<slug:slug>/', views.WorkerDetailView.as_view(), name='tools_list'),
    path('worker/', views.WorkerCreateView.as_view(), name='worker_create'),
    path('tool/', views.ToolsCreateView.as_view(), name='tool_create')
]
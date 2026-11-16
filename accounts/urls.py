from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_redirect),
    path('teacher/', views.teacher_dashboard),
    path('student/', views.student_dashboard),
    path('admin/', views.admin_dashboard),
]
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .decorators import role_required


@role_required('TEACHER')
def teacher_dashboard(request):
    return render(request, 'dashboard.html')


@role_required('STUDENT')
def student_dashboard(request):
    return render(request, 'dashboard.html')


@role_required('ADMIN')
def admin_dashboard(request):
    return render(request, 'dashboard.html')

def dashboard_redirect(request):

    if not request.user.is_authenticated:
        return redirect('/auth/login/')

    role = request.user.role

    if role == 'ADMIN':
        return redirect('/accounts/admin/')

    elif role == 'TEACHER':
        return redirect('/accounts/teacher/')

    elif role == 'STUDENT':
        return redirect('/accounts/student/')

    return HttpResponse("Invalid User Role", status=403)
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()

    search = request.GET.get('search')
    department = request.GET.get('department')

    if search:
        students = students.filter(name__icontains=search)

    if department:
        students = students.filter(department=department)

    departments = Student.objects.values_list(
        'department', flat=True
    ).distinct()

    return render(request, 'students/student_list.html', {
        'students': students,
        'departments': departments,
    })

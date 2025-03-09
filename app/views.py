from django.shortcuts import render, redirect
from . import models

## Pages

# /
def index(request):
  records = models.Student.objects.all()
  print(records)
  return render(request, 'index.html',  { 'students': records })

# /create-student
def create_student_page(request):
  return render(request, 'create-student.html')

# /update-student/<int:student_id>
def update_student_page(request, student_id):
  student = models.Student.objects.get(StudentID=student_id)
  return render(request, 'update-student.html', { 'student': student })

# /view-student/<int:student_id>
def view_student_page(request, student_id):
  student = models.Student.objects.get(StudentID=student_id)
  return render(request, 'view-student.html', { 'student': student })

# /confirm-delete/<int:student_id>
def confirm_delete_page(request, student_id):
  student = models.Student.objects.get(StudentID=student_id)
  return render(request, 'confirm-delete.html', { 'student': student })

## API Endpoints

# /api/create-student
def create_student(request):

  if request.method == "POST":
    required_fields = ["student_id", "first_name", "last_name", "email", "date_of_birth", "course", "enrollment_date"]
    data = {field: request.POST.get(field) for field in required_fields}

    record = models.Student(
        StudentID=data["student_id"],
        FirstName=data["first_name"],
        LastName=data["last_name"],
        Email=data["email"],
        DateOfBirth=data["date_of_birth"],
        Course=data["course"],
        EnrollmentDate=data["enrollment_date"],
    )

    record.save()
    return redirect('/')
    

# /api/update-student
def update_student(request):
  if request.method == "POST":

    required_fields = ["student_id", "first_name", "last_name", "email", "date_of_birth", "course", "enrollment_date"]
    data = {field: request.POST.get(field) for field in required_fields}
    record = models.Student.objects.get(StudentID=data['student_id'])

    # Update record
    record.FirstName = data['first_name']
    record.LastName = data['last_name']
    record.Email = data['email']
    record.DateOfBirth = data['date_of_birth']
    record.Course = data['course']
    record.EnrollmentDate = data['enrollment_date']
    record.save()

    return redirect('/')
  
# /api/delete-student
def delete_student(request):
  if request.method == "POST":

    # Delete record
    record = models.Student.objects.get(StudentID=request.POST.get('student_id'))
    record.delete()

    return redirect('/')
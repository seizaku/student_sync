
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('create-student', views.create_student_page, name="create_student_page"),
  path('update-student/<int:student_id>', views.update_student_page, name="update_student_page"),
  path('view-student/<int:student_id>', views.view_student_page, name="view_student_page"),
  path('confirm-delete/<int:student_id>', views.confirm_delete_page, name="confirm_delete_page"),
  path('api/create-student', views.create_student, name="create_student"),
  path('api/update-student', views.update_student, name="update_student"),
  path('api/delete-student', views.delete_student, name="delete_student"),
]
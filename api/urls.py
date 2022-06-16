from django.urls import path
from . import views

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from school.models import Student,School
from .serializers import StudentSerializer, SchoolSerializer

urlpatterns = [
    path('downloadStudent.csv', views.student_csv, name='student_csv'),
    path('downloadSchool.csv', views.school_csv, name='school_csv'),
    path('students/', ListCreateAPIView.as_view(queryset=Student.objects.all(), serializer_class=StudentSerializer), name='student-list'),
    path('schools/', ListCreateAPIView.as_view(queryset=School.objects.all(), serializer_class=SchoolSerializer), name='school-list'),

    path('students/<int:pk>/', views.StudentList.as_view()),
    path('schools/<int:pk>/', views.SchoolList.as_view()),
    # path('students/', views.getStudents),
    # path('schools/', views.getSchools),
    # path('addStudent/', views.addStudent),
    # path('addSchool/', views.addSchool),
    # path('students/<int:pk>/', views.getStudent),
    # path('schools/<int:pk>/', views.getSchool),

    path('schools/<int:pk>/students', views.StudentInSchool.as_view()),
    # path('schools/<int:pk>/addStudent', views.addStudentInSchool),
    # path('Dstudents/<int:pk>/', views.deleteStudent),
    # path('Dschools/<int:pk>/', views.deleteSchool),

    #path('s/<int:id>', ),
    #path('schools/<int:id>/students', views.addStudent),
    #path('students/', views.addStudent),
]
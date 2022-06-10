from rest_framework.response import Response
from rest_framework.decorators import api_view
from school.models import Student,School
from .serializers import StudentSerializer, SchoolSerializer


from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class StudentList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.all()

class SchoolList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    def get_queryset(self):
        return School.objects.all()

class StudentInSchool(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        #print(Student.objects.select_related('school_id'))
        return Student.objects.select_related('school_id')
    # def create(self, request, *args, **kwargs):
    #     print(args)
    #     serializer = StudentSerializer(data = request.data)
    #     return Response(serializer.data)

    # def get(self,request,pk,format=None):
    #     student = Student.objects.filter(school_id=pk)
    #     serializer = StudentSerializer(student, many=True)
    #     return Response(serializer.data)
    # def create(self,request,pk,format=None):
    #     print(request.data['school_id'])
    #     request.data['school_id']=pk
    #     serializer = StudentSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)


# def get(self,request,pk,format=None):
#     country=self.get_object(pk)
#     serializer=CountrySerializer(country)
#     return Response(serializer.data,status=status.HTTP_200_OK)
# def put(self,request,pk,format=None):
#     country=self.get_object(pk)
#     serializer=CountrySerializer(country,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# def delete(self,request,pk,format=None):
#     country=self.get_object(pk)
#     country.delete()
#########################################################################


# @api_view(['GET'])
# def getStudents(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getSchools(request):
#     schools = School.objects.all()
#     serializer = SchoolSerializer(schools, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addStudent(request):#old
#     serializer = StudentSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def addSchool(request):
#     serializer = SchoolSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)




# @api_view(['GET'])
# def getStudent(request,pk):
#     student = Student.objects.get(id=pk)
#     serializer = StudentSerializer(student, many=False)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getSchool(request,pk):
#     schools = School.objects.get(id=pk)
#     serializer = SchoolSerializer(schools, many=False)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getStudentInSchool(request,pk):
#     student = Student.objects.filter(school_id=pk)
#     #print(student)
#     #print(len(student))
#     #print(School.objects.get(id=pk).max_student)
#     serializer = StudentSerializer(student, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addStudentInSchool(request,pk):
#     #student = Student.objects.filter(school_id=pk)
#     request.data["school_id"] = pk

#     serializer = StudentSerializer(data = request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['GET'])
# def deleteStudent(request,pk):
#     student = Student.objects.get(id=pk)
#     student.delete()
#     return Response("Student was deleted")

# @api_view(['GET'])
# def deleteSchool(request,pk):
#     schools = School.objects.get(id=pk)
#     school.delete()
#     return Response("School was deleted")
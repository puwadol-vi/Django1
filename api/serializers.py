from rest_framework import serializers
from school.models import Student,School

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def validate(self, data):
        school = data['school_id']
        if len(Student.objects.filter(school_id=school.id))==school.max_student:
            raise serializers.ValidationError("maximum number of student reached")
        return data

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

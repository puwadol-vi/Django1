from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import School,Student
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','student_id','school_id')
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.strip().split(",")
                if len(fields)==1: continue
                if 'first_name' == fields[0] and 'last_name' == fields[1] and 'student_id' == fields[2]: continue
                print(fields)
                created = Student.objects.update_or_create(
                    first_name = fields[0],
                    last_name = fields[1],
                    student_id = fields[2],
                    school_id = School.objects.get(school_name=fields[3]),
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_name', 'max_student')
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.strip().split(",")
                if len(fields)==1: continue
                if 'school_name' == fields[0] and 'max_student' == fields[1]: continue
                # school = School.objects.get(school_name=fields[0])
                # if school:
	               #  school.max_student=fields[1]
	               #  school.save()
                # else:
                created = School.objects.update_or_create(
                    school_name = fields[0],
                    max_student = fields[1],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
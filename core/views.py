from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import AddstudentForm

# Create your views here.

class Home(View):
    def get(self, request):
        stu_data= Student.objects.all()
        return render(request, 'core/home.html', {'studata':stu_data})


class Add_Student(View):
    def get(self,request):
        fm= AddstudentForm()
        return render(request,'core/add-student.html',{'form':fm})

    def post(self,request):
        fm= AddstudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/add-student.html',{'form':fm})

class Delete_Student(View):
    def post(self,request):
        data = request.POST
        id= data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')


class UPdate_student(View):
    def get(self,request,id):
        stu = Student.objects.get(id=id)
        fm= AddstudentForm(instance=stu)
        return render(request,'core/update_student.html',{'form':fm})
        
    def post(self,request,id):
         stu = Student.objects.get(id=id)
         fm= AddstudentForm(request.POST,instance=stu)
         if fm.is_valid():
            fm.save()
            return redirect('/')





  

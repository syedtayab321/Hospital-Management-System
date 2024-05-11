from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Doctor_Details
# Create your views here.
def index(request):
        return render(request,'index.html')

def admin_login(request):
        # return render(request,'admin_related/login.html')
        return render(request,'admin_related/admin_dashboard.html')
        

def admin_dashboard(request):
        email=request.POST['email']
        password=request.POST['password']
        data={
                "error":"wrong cridentials"
        }
        if email=='admin321@gmail.com' and password=='roomb343':
                return render(request,'admin_related/admin_dashboard.html')
        else:
                return render(request,'admin_related/login.html',data)
                
def forgot_password(request):
        return render(request,'admin_related/forgot_password.html')

# adding doctor data to form

def add_doctor(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
        #  email = request.POST['email']
            age = request.POST['age']
            specialist = request.POST['specilist'] 
            date = request.POST['date']
            code = request.POST['mobile']
            number = request.POST['number']
            mobile_number = code + number
            Doctor_Details.objects.create(
                name=name,
                email="tayab5@gmail.com",
                age=age,
                specilist=specialist,
                date=date,
                mobile_number=mobile_number
            )
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        except KeyError:
            # Handle the case where one of the POST keys is missing
            return HttpResponse("Incomplete form data. Please fill in all required fields.", status=400)
    return render(request, 'admin_related/admin_dashboard.html')

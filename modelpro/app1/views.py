from django.shortcuts import render,redirect
from .models import Employee
# Changes done 
# Create your views here.
def index(request):
    data = Employee.objects.all()
    print(data)
    return render(request,"index.html",{'data':data})
    
def add_data(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            salary = request.POST['salary']
            gender = request.POST['gender']
            department = request.POST['department']
            image = request.FILES['image']
            data = Employee.objects.create(name=name,email=email,dept=department,contact=contact,salary=salary,gender=gender,image=image)
            data.save()
            return redirect('index')
        except:
            return render(request,"addform.html")
    else:
        return render(request,"addform.html")

def delete_data(request,email):
    data = Employee.objects.filter(email=email)
    data.delete()
    return redirect('index')

def update_data(request , email):
    data = Employee.objects.get(email=email) #get return data && filter return queryset
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            salary = request.POST['salary']
            gender = request.POST['gender']
            department = request.POST['department']
            image = request.FILES['image']
            data = Employee.objects.filter(email=email)
            data.update(name = name, email = email, dept = department, contact = contact, salary = salary, gender = gender, image=image)
            return redirect('index')
        except:
                return render(request,"updateform.html",{'data':data})
    return render(request,"updateform.html",{'data':data})



def search_data(request):
    if request.method == "POST":
        value = request.POST['search']
        data = Employee.objects.filter(name__iexact = value)
        if data is not None:
            return render(request,"index.html",{'data':data})
        else:
            data = Employee.objects.all()
            return render(request,"index.html",{'data':data})
    else:
        return render(request,"index.html")

def search_male(request):
    data = Employee.objects.filter(gender__iexact = 'male')
    return render(request,"index.html",{'data':data})

def search_female(request):
    data = Employee.objects.filter(gender__iexact = 'female')
    return render(request,"index.html",{'data':data})

def show_all_data(request):
    data = Employee.objects.all()
    return render(request,"index.html",{'data':data})

# def search_manager(request):
#     data = Employee.objects.filter(dept__iexact = 'manager')
#     return render(request,"index.html",{'data':data})

# def search_designer(request):
#     data = Employee.objects.filter(dept__iexact = 'designer')
#     return render(request,"index.html",{'data':data})

# def search_administration(request):
#     data = Employee.objects.filter(dept__iexact = 'administration')
#     return render(request,"index.html",{'data':data})

# def search_system_administration(request):
#     data = Employee.objects.filter(dept__iexact = 'system_administration')
#     return render(request,"index.html",{'data':data})

# def search_security_administration(request):
#     data = Employee.objects.filter(dept__iexact = 'security_administration')
#     return render(request,"index.html",{'data':data})

# def search_application_developer(request):
#     data = Employee.objects.filter(dept__iexact = 'applisearch_application_developer')
#     return render(request,"index.html",{'data':data})

# def search_database_administration(request):
#     data = Employee.objects.filter(dept__iexact = 'database_administration')
#     return render(request,"index.html",{'data':data})

# def search_web_developer(request):
#     data = Employee.objects.filter(dept__iexact = 'web_developer')
#     return render(request,"index.html",{'data':data})

# def search_helpdesk_supporter(request):
#     data = Employee.objects.filter(dept__iexact = 'helpdesk_supporter')
#     return render(request,"index.html",{'data':data})

# def search_technical_supporter(request):
#     data = Employee.objects.filter(dept__iexact = 'technical_supporter')
#     return render(request,"index.html",{'data':data})

def search_dept(request):
    dpt = request.GET.get('dpt')
    if dpt == 'manager':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'designer':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'administration':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'system_administration':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'security_administration':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'application_developer':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'database_administration':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'web_developer':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'helpdesk_supporter':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})
    if dpt == 'technical_supporter':
        data = Employee.objects.filter(dept__iexact=dpt)
        return render(request,"index.html",{'data':data})

def filter_salary(request):
    min = float(request.GET.get('min'))
    max = float(request.GET.get('max'))
    data = Employee.objects.filter(salary__range=(min,max))
    return render(request,"index.html",{'data':data})

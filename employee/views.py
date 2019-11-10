from django.shortcuts import render, redirect  
import pyrebase
from employee.forms import EmployeeForm  
from employee.models import Employee  
## Create your views here.  


config ={
        'apiKey': "AIzaSyBpy-7yVY4Nmgt26R-R7i_b7pgQDSo73kE",
        'authDomain': "gaslp-842a6.firebaseapp.com",
        'databaseURL': "https://gaslp-842a6.firebaseio.com",
        'projectId': "gaslp-842a6",
        'storageBucket': "",
        'messagingSenderId': "429233000110",
        'appId': "1:429233000110:web:fbaf86f7f00c501b91a73f"
                                }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def login(request):
        return render(request, "core/login.html")


def visitas(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "Credenciales invalidas"
        return render(request,"core/login.html",{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "core/visitas.html",{"e":email})


def visitas2(request):
    return render(request, "core/visitas.html")



def clientes(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/clientes')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "core/clientes.html", {'form': form})
    #return render(request, "core/clientes.html", {'form': cliente_form})


def compras(request):
    return render(request, "core/compras.html")


def ventas(request):
    return render(request, "core/ventas.html")

def reportes(request):
    return render(request, "core/reportes.html")



def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'core/clientes.html',{'form':form})  

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"core/show.html",{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'core/edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'core/edit.html', {'employee': employee})  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

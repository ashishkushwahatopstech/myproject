from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *
# Create your views here.

def index(request):
    all = Register.objects.all()
    if request.method == 'POST':
        data = request.POST
        email = data.get("email")
        phone = data.get("phone")

        Register.objects.create(
            Email = email,
            Contact = phone
        )
        return redirect("index")
    return render(request, "index.html",{"Registers":all})



def employee(request):
    E_all = Employee.objects.all()
    if request.method == "POST":
        data = request.POST
        id = data.get("id")
        fname = data.get("f_name")
        mname = data.get("m_name")
        lname = data.get("l_name")
        m_status = data.get("marital_status")
        email = data.get("email")
        contact = data.get("contact")
        add = data.get("address")

        Employee.objects.create(
            F_name = fname,
            M_name = mname,
            L_name = lname,
            Martial_status = m_status, 
            Email = email,
            Contact = contact,
            Address = add
        )
        return redirect("employee")
    # did = request.GET.get('did')
    did = request.GET.get('did')
    if did:  # Only delete if 'did' is provided
        employee_to_delete = get_object_or_404(Employee, id=did)
        employee_to_delete.delete()
        return redirect("employee")
    return render(request, "employee.html",{"E_all":E_all})



def product(request):
    return render(request, "product.html")



def contact(request):
    return render(request, "contact.html")



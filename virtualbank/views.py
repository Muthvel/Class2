from django.shortcuts import redirect, render
from . models import Customer
from . forms import SignupForm
from . forms import SignupModelForm
from django.contrib.auth.hashers import make_password

# Create your views here.
def welcome(request):
    context = {"name": "Rajesh"}
    return render(request, 'virtualbank/welcome.html', context)

def greeting(request):
    return render(request, 'virtualbank/greeting.html')

def sign_up(request):
    signupForm = SignupForm()
    context = {"form":signupForm}
    cust_name = ''
    if request.method == "POST":
        signupForm = SignupForm(request.POST)
        context = {"form":signupForm}
        if signupForm.is_valid():
            cust_name = request.POST.get("user_name")
            password = make_password(request.POST.get("password"))
            email = request.POST.get("email")
            new_customer = Customer()
            new_customer.name = cust_name
            new_customer.email = email
            new_customer.password = password
            new_customer.save()
            context = {"name":cust_name}
    if cust_name:
        return redirect('/success')
    return render (request, 'virtualbank/sign_up.html', context)

def sign_up_with_model_form(request):
    signupForm = SignupModelForm()
    context = {"form":signupForm}
    if request.method == "POST":
        signupForm = SignupModelForm(request.POST)
        context = {"form":signupForm}
        if signupForm.is_valid():
            signupForm.cleaned_data['password'] = make_password(signupForm.cleaned_data['password'])
            signupForm = SignupModelForm(signupForm.cleaned_data)
            signupForm.save()
            return redirect('/success')
    return render (request, 'virtualbank/sign_up.html', context)

def success(request):
    return render(request, "virtualbank/success.html")


def list_one(request):
    one_customer = Customer.objects.first()
    context = {"customer": one_customer}
    return render (request, 'virtualbank/list_one.html', context)

def list_all(request):
    customers = Customer.objects.all()[0:5]
    context = {"customers": customers}
    return render (request, 'virtualbank/list_all.html', context)

def list_n(request, n):
    customers = Customer.objects.all()[0:n]
    context = {"customers": customers}
    return render (request, 'virtualbank/list_all.html', context)

def clickable_list(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render (request, 'virtualbank/list_clickable.html', context)

def list_particular(request, id):
    one_customer = Customer.objects.get(pk=id)
    context = {"customer": one_customer}
    return render (request, 'virtualbank/list_one.html', context)


def get_by_id_from_browser_form(request):
    cutomerId = request.GET.get('customerId')

    if cutomerId:
        one_customer = Customer.objects.get(pk= cutomerId)
        context = {"customer": one_customer}
        return render (request, 'virtualbank/list_one.html', context)
    return render (request, 'virtualbank/get_one.html')

def filter_name_contains(request):
    searchName = request.GET.get('customer_name')
    if searchName:
        customers = Customer.objects.filter(name=searchName)
        print(customers.__len__())
        context = {"customers": customers}
        if customers.__len__() == 0:
            return render (request, 'virtualbank/norecordsfound.html')
        return render (request, 'virtualbank/list_clickable.html', context)
    return render (request, 'virtualbank/list_clickable.html')
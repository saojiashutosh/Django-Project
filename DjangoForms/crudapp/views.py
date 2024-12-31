from django.shortcuts import redirect, render
from .models import customer

# Create your views here.
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            obj = customer(cust_name=form.cleaned_data.get('cust_name'), cust_contact=form.cleaned_data.get('cust_contact'))
            obj.save()
        else:
            print('Validation Failed...')
    
    form = RegisterForm()
    objs = customer.objects.all()

    return render(request, 'crudapp/register.html', {'form':form, 'data': objs})

def update(request,id):
    if request.method=='POST':
        obj = customer.objects.get(id=request.POST.get('id'))
        obj.cust_name = request.POST.get('name')
        obj.cust_contact = request.POST.get('contact')
        obj.save()
        
        return redirect('/')
    if not id :
        return redirect('/') 
    obj = customer.objects.get(id=id)
    return render(request, 'crudapp/update.html', {'obj': obj})


def delete(request,id):
    if id:
        obj = customer.objects.get(id=id)
        obj.delete()
    return redirect('/')
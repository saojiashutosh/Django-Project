from django.shortcuts import redirect, render
from .models import customer

# Create your views here.
def register(request):
    if request.method=='POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        obj = customer(cust_name=name, cust_contact=contact)
        obj.save()
    
    objs = customer.objects.all()
    return render(request, 'crudapp/register.html', {'data': objs})

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
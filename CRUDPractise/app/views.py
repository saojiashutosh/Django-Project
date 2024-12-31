from django.shortcuts import get_object_or_404, redirect, render
from .models import User

# Create your views here.
def signup(request):
    data = User.objects.all()
    return render(request,"app/index.html",{'data':data})

def update(request, id):  # Ensure `id` is explicitly included as a parameter
    if request.method =='POST':
        obj = User.objects.get(id=request.POST.get('id'))
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.address = request.POST.get('address')
        obj.save()
        return redirect('/')
    if not id:
        return redirect('/')
    
    obj = User.objects.get(id=id)
    return render(request, 'app/update.html', {'obj': obj})
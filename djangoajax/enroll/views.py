from django.shortcuts import render
from .forms import UserForm
from.models import User
from django.http import JsonResponse

# Create your views here.

def home(request):
    form = UserForm()
    stud = User.objects.all()
    return render(request,'enroll/home.html',{'form':form,'stud':stud})

def save_data(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            id = request.POST.get('id')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (id == ''):
            # usr = User.objects.create(name=name,email=email,password=password)
                usr = User(name=name,email=email,password=password)
            else:
                usr = User(id=id,name=name,email=email,password=password)
            usr.save()
            user = list(User.objects.values())
            return JsonResponse({'status':201,'user':user})
        else:
            return JsonResponse({'status':400})
        
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        usr = User.objects.get(pk=id)
        usr.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        usr = User.objects.get(pk=id)
        data = {'id':usr.id,'name':usr.name,'email':usr.email,'password':usr.password}
        return JsonResponse(data)

        


from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
from .models import UserProfile
from .forms import UserForm,SignInForm,UserProfileForm

def home(request):
    user = request.user
    
    return render(request,'home.html')

def profile(request):
    user=request.user
    obj=0
    
    try:
        obj, created = UserProfile.objects.get_or_create(user=user)
        
    except:
        pass
 
    return render(request,'profile.html',{'obj':obj,'user_d':user})




def user_profile_update(request):
    user=request.user
    user_instance = User.objects.get(id=user.id)
    obj=0
    
    
    try:
        obj, created = UserProfile.objects.get_or_create(user=user_instance)
        
    except:
        pass
    
    if request.method=="POST" and obj:
        form=UserProfileForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('profile')
    elif request.method=="POST":
        form=UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user=request.user
            form2.save()
            return redirect('profile')
    

    elif obj:
        form=UserProfileForm(instance=obj)
    else:
        form=UserProfileForm()
    return render(request,"user_profile.html",{'form':form})













def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SignIn')
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})

def SignIn(request):   
    if request.method=="POST":
        form=SignInForm(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if not user:
                messages.warning(request,'The User Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            if user:
                
                login(request, user)
                return redirect('home')
    else:
        form=SignInForm()
    return render(request,'login.html',{'form':form})

def logout_f(request):
    logout(request)
    return redirect('SignIn')
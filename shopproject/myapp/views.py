from django.shortcuts import render,redirect
from  .forms import signupForm
from .models import signup
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("signup successfully")
            
                #email sending
                sub='Welcome !'
                msg='Dear user '
                from_email='darshitgajjar2@gmail.com'
                to_email=[request.POST['Email address']]
                send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
                return redirect('about')

            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['Email address']
            pas=request.POST['Password']
            user=signup.objects.filter(Email=unm,Password=pas)
            if user:
                print('login succfunlly')
                request.session['Email address']=unm
                return redirect('notes')
                
            else:
                print('Eror to Email and Password does not match')
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')
def products(request):
    return render(request,'products.html')
def fashion(request):
    return render(request,'fashion.html')
def showdatapage(request):
    return render(request,'showdatapage.html')
def notes(request):
    Emailaddress=request.session.get('Email address')
    return render(request,'notes.html',{'Email address':'Email address'})

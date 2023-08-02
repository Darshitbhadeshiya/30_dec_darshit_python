from django.shortcuts import render,redirect
from .forms import signupForm,contactForms
from .models import user
from django. core. mail import send_mail
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.method=='POST': #root 
        if request.POST.get('signup')=='signup': #sigup 
            print('check.................................!!!!!!!!!!!')
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("admin succfully")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':  #Login
            print('check!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            unm=request.POST['email']
            pas=request.POST['password']
            abc=user.objects.filter(email=unm,password=pas)
            if abc: #true
                print('Login succfully')
                request.session['email'] = unm
                return redirect('notes')
            else:
                print('login email and password does not match')
        
    return render(request,'index.html')

def note(request):
    user=request.session.get('email')
    return render(request,'note.html' ,{'user':user})

def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        newcontact=contactForms(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("your forms has been submit")
            #send email
            sub='thank you'
            msg=f"Thank you for connecting with us!\nWe will assist you in near future.\n\nPlease contact us on \n+91 9724799469 | notesapp@support.com | Sanket Chauhan - Sr.Trainer | TOPS Tech"
            fromEmail=settings.EMAIL_HOST_USER
            toEmail=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=fromEmail,recipient_list=toEmail)
            
        else:
            print(newcontact.errors)


    return render(request,'contact.html')
def profile(request):
    return render(request,'profile.html')

def lgout(request):
    logout(request)
    return redirect('/')
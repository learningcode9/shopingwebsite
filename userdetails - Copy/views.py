from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from userdetails.forms import signupForm,loginForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
#from utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .token_generator import generate_token


# Create your views here.
def Register(request):
    if request.method == 'POST':
       
        form=signupForm(request.POST)#with the form data creating an object,when ever form submits then only this if part works.
        if  form.is_valid():#if form values are valid ,means without any errors
            
            first_name=form.cleaned_data['first_name'] #capturing the data from the form fields
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            #confirm_password=form.cleaned_data['confirm_password']
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            current_site=get_current_site(request)
            email_subject='Activate your account',
            message=render_to_string('activate.html',
            {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user)
            })
            email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    
                )
            email_message.send()
            return redirect('login')

    else:
        form=signupForm()
        response=render(request,'Register.html',{'form':form})
        response.set_cookie('firstname','bellam')
        return response

def ActivateAccount(request,uidb64,token):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except Exception as identifier:
        user=None
    if user is not None and generate_token.check_token(user,token):
        user.is_active=True
        user.save()
        messages.add_message(request,messages.INFO,'account activates successfully')
        return redirect('login')
    return render(request,'activate_failed.html')

        

def login(request):
    if request.method=='POST':
        form=loginForm(request.POST)
        print(form)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request,user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else: 
                messages.error(request, "Invalid username or password.")
                return redirect('login')
        
    else:
        form = loginForm()
        return render(request,"login.html",{"form":form})


def logout(request):
    auth.logout(request)
    return redirect("/")
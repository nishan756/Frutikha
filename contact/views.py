from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from about_us.models import AboutUs
from .models import Subscribe
# Create your views here.

def get_email():
    return AboutUs.objects.first().email

def ContactUs(request):
    if request.method == 'POST':
        form  = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thanks for conatct with us!')
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            from_email = get_email()
            send_mail(
                subject = subject,
                message = 'We recieved your message, We will reply your message within 7 days via this email',
                recipient_list = [email,],
                fail_silently = False,
                from_email = from_email,

            )
            return redirect('all-product')
        else:
            messages.error(request,'Something went wrong')
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})

def SubscribeUs(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            new_subscriber = Subscribe(email = email)
            new_subscriber.save()
            send_mail(
                subject = 'Thanks for subscribe us',
                from_email = get_email(),
                fail_silently = False,
                recipient_list = [email,],
                message = 'Hi, Thanks for subscribe us! We will notify  update news via this email'
            )
        except Exception as e:
            return render(request,'404.html',{'message':'An error occurred'})
        return redirect('home')

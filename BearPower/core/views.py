from django.shortcuts import render, redirect
from .models import Home, About, Question, Features, CTA, Gallery, Testimonial
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def home(request):
    home = Home.objects.all()[0]
    about = About.objects.all()[0]
    question = Question.objects.all()
    features = Features.objects.all()[0]
    data = CTA.objects.all()[0]
    images = Gallery.objects.all()
    humans = Testimonial.objects.all()
    context ={
        'home': home,
        'about': about,
        'question': question,
        'feature': features,
        'data': data,
        'images': images,
        'humans': humans
    }
    return render(request, 'index.html', context)

    
def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            send_mail(
                subject='New Newsletter Subscriber',
                message=f'A new user has subscribed to your newsletter: {email}',
                from_email=None,  
                recipient_list=['bearpowernig@gmail.com'],  
            )

            send_mail(
                subject='Welcome to BearPower ☀️',
                message="""
Thanks for subscribing to BearPower!

We're excited to have you on board as we work toward a cleaner, brighter, and more sustainable future powered by solar energy.

Stay tuned for updates, tips, and special offers — all delivered straight to your inbox.

The BearPower Team💚
                """,
                from_email=None,
                recipient_list=[email],
            )
            messages.success(request, "You've been subscribed successfully!")
        else:
            messages.error(request, "Please enter a valid email.")
    return redirect('home')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

           
            send_mail(
                subject=f"Contact Form: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\n{message}",
                from_email=None,
                recipient_list=['bearpowernig@gmail.com'],  
            )

            
            send_mail(
                subject='Thanks for reaching out to BearPower ⚡',
                message=f"""
Hi {name},

Thanks for contacting BearPower! We've received your message and will get back to you shortly.

If your request is urgent, feel free to reply to this email directly.

Best regards,  
The BearPower Team💚
                """,
                from_email=None,
                recipient_list=[email],
            )

            messages.success(request, "Your message was sent successfully!")
            return redirect('home')  

    return render(request, 'index.html', {'form': form})


def about(request):
    about = About.objects.all()[0]
    context={
        'about': about
    }
    return render(request,'about.html', context)

def service(request):
    
    context={
        
    }
    return render(request,'service.html', context)


def gallery(request):
    images = Gallery.objects.all()
    context={
        'images': images,
    }
    return render(request,'gallery.html', context)

def contact_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

           
            send_mail(
                subject=f"Contact Form: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\n{message}",
                from_email=None,
                recipient_list=['bearpowernig@gmail.com'],  
            )

            
            send_mail(
                subject='Thanks for reaching out to BearPower ⚡',
                message=f"""
Hi {name},

Thanks for contacting BearPower! We've received your message and will get back to you shortly.

If your request is urgent, feel free to reply to this email directly.

Best regards,  
The BearPower Team💚
                """,
                from_email=None,
                recipient_list=[email],
            )

            messages.success(request, "Your message was sent successfully!")
            return redirect('home')  
    return render(request, 'contact.html')
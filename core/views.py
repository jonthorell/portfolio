from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,View
from django import forms
from core.forms import ContactForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

class index(TemplateView):
    '''Class used to display the index page '''

    template_name = 'core/index.html'
    
class encyclopedia(TemplateView):
    '''Class used to display the encyclopedia page '''

    template_name = 'core/encyclopedia.html'
    
class projects(TemplateView):
    '''Class used to display the projects page '''

    template_name = 'core/projects.html'
    
class quiz(TemplateView):
    '''Class used to display the quiz page '''

    template_name = 'core/quiz.html'
    
class pirate_island(TemplateView):
    '''Class used to display the Pirate Island page '''

    template_name = 'core/pirate_island.html'
    
class retro(TemplateView):
    '''Class used to display the RetroLovers page '''

    template_name = 'core/retro.html'
    
class synth(TemplateView):
    '''Class used to display the synth.nu page '''

    template_name = 'core/synth.html'
    
class portfolio(TemplateView):
    '''Class used to display the portfolio page '''

    template_name = 'core/portfolio.html'
    
class about(TemplateView):
    '''Class used to display the about page '''

    template_name = 'core/about.html'
    
class contact(View):
    '''Class used to display the contact page '''

    template_name = 'core/contact.html'
    
    def post(self, request, *args, **kwargs):
        # display form
        form = ContactForm(request.POST)
        if form.is_valid():
            # notify user
            messages.info(request, "Thank you. Your response has been received.")
            # get form values into variables
            req_user = request.POST.get("name")
            req_mess = request.POST.get("mess")
            req_email = request.POST.get("email")
            req_subject = request.POST.get("subject")        

            # set variables for e-mail.
            subject = 'Mail from Synth.Nu'
            message = f'Hi { req_user }, your issue has been received. We will look into it as soon as possible.\nThe message you submitted was { req_mess }. with the subject line { req_subject }'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [req_email, ]
            # send the mail. Notify the user and return to start page
            # send_mail( subject, message, email_from, recipient_list )
            # messages.info(request, "Check your e-mail.")
            return HttpResponseRedirect("/")
    def get(self, request, *args, **kwargs):
        # display form
        
        form = ContactForm(request.POST)
        return render(
        request,
        "core/contact.html",
        {"form": form},
    )
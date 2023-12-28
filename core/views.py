from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

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
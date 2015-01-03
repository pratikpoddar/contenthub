from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

try:
    ### some code to be executied on server start and variables imported in views
    pass
except:
    pass

def index(request):
    return render(request, 'flip/base.html', {})


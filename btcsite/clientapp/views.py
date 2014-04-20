from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def welcome_page(request):
    now = datetime.datetime.now()
    t = get_template('v1/index.html')
    html = t.render(Context({'time': now}))
    return HttpResponse(html)
    # return render_to_response('time.html', locals())

def sign_in(request):
    #html = request.GET.get('email')
    now = datetime.datetime.now()
    t = get_template('v1/sign_in.html')
    html = t.render(Context({'time': now}))
    return HttpResponse(html)

def sign_up(request):
    html = request.GET.get('email')
    return HttpResponse(html)

def forget_password(request):
    html = "Please create a new one..."
    return HttpResponse(html)
#def index_css(request):
#    return render_to_response('static/css/index.css', locals())

def sample_form(request):
    now = datetime.datetime.now()
    t = get_template('v1/sample_form.html')
    html = t.render(Context({'time': now}))
    return HttpResponse(html)

def status(request):
    now = datetime.datetime.now()
    t = get_template('v1/status.html')
    html = t.render(Context({'time': now}))
    return HttpResponse(html)


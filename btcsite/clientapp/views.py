from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from backend.getTransaction import get_tx
import datetime
import json

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

def creditor_form(request):
    now = datetime.datetime.now()
    t = get_template('v1/creditor_form.html')
    html = t.render(Context({'time': now}))
    return HttpResponse(html)

def creditor_status(request):
    ownerkey = request.GET['ownerkey']
    num_months = request.GET['num_months']
    total_value = request.GET['total_value']
    creditor_addr = request.GET['creditor_addr']
    buyer = request.GET['buyer']
    
    now = datetime.datetime.now()
    t = get_template('v1/creditor_status.html')
    html = t.render(Context(
    {'time': now, 
    'ownerkey': ownerkey, 'num_months': num_months, 
    'total_value': total_value, 'creditor_addr': creditor_addr, 
    'buyer': buyer}))
    return HttpResponse(html)

def buyer_form(request):
    now = datetime.datetime.now()
    t = get_template('v1/buyer_form.html')
    html = t.render(Context({'time': now}))
    return HttpResponse(html)

def buyer_status(request):
    tx_hash = request.GET['tx_hash']
    tx_index = request.GET['tx_index']
    buyer_key = request.GET['buyer_key']
    creditor = request.GET['creditor']
    
    now = datetime.datetime.now()
    t = get_template('v1/buyer_status.html')
    html = t.render(Context(
    {'time': now, 
    'tx_hash': tx_hash, 'tx_index': tx_index, 
    'buyer_key': buyer_key, 'creditor': creditor}))
    return HttpResponse(html)
    
def car_form(request):
    now = datetime.datetime.now()
    t = get_template('v1/car_form.html')
    html = t.render(Context({'time': now}))
    return HttpResponse(html)

def car_status(request):
    tx = request.GET['tx']
    returnType = request.GET['type']
    result = get_tx(tx, returnType)
    now = datetime.datetime.now()
    t = get_template('v1/car_status.html')
    html = t.render(Context(
    {'time': now, 'tx': result}))
    return HttpResponse(html)

from django.conf.urls import patterns, include, url
from clientapp.views import current_datetime
from clientapp.views import welcome_page
from clientapp.views import sign_in
from clientapp.views import sign_up
from clientapp.views import forget_password
from clientapp.views import creditor_form, creditor_status
from clientapp.views import buyer_form, buyer_status
from clientapp.views import car_form, car_status
#from clientapp.views import index_css

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'btcsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index.html$', welcome_page),    
    #url(r'^static/css/index.css', index_css),
    url(r'^time/', current_datetime),
    url(r'signIn/', sign_in),
    url(r'signUp/', sign_up),
    url(r'forgetPassword/', forget_password),
    url(r'creditorForm/', creditor_form),
    url(r'creditorStatus/', creditor_status),
    url(r'buyerForm/', buyer_form),
    url(r'buyerStatus/', buyer_status),
    url(r'carForm/', car_form),
    url(r'carStatus/', car_status),
)

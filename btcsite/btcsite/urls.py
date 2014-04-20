from django.conf.urls import patterns, include, url
from clientapp.views import current_datetime
from clientapp.views import welcome_page
from clientapp.views import sign_in
from clientapp.views import sign_up
from clientapp.views import forget_password
from clientapp.views import sample_form
from clientapp.views import transaction
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
    url(r'sampleForm/', sample_form),
    url(r'transaction/', transaction),
)

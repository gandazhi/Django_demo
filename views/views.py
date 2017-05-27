# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
import datetime

# Create your views here.

def hello(request):
    return HttpResponse('hello world')

def date(request):
    now = datetime.datetime.now()
    # html = '<html><body>It is now %s.</body></html>' %now
    # assert False
    return render_to_response('date_app/date.html', {'current_date': now})

def add(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    c = a + b
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
    demo_list = ['java', 'php', 'python']
    List = map(str, range(100))
    return render(request, 'home.html', {'List': List})

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


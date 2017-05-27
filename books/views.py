# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from books.models import Publisher
# Create your views here.


def create_db(request):
    p1 = Publisher.objects.create(name='gandazhi', address='2855', city='chengdu', state_province='四川', country='CN',
                                  website='http://www.apress.com/')
    p1.address = '230,high,chengdu'
    p1.website = 'http://www.google.com'
    p1.save()
    return HttpResponse('hello db2')
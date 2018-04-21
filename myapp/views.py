# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import MessageForm
from .models import Messsge


# from django.core.paginator import Paginator


# Create your views here.

class Main(View):
    def get(self, request):
        obj = Messsge.objects.all().filter()
        return render(request, 'message.html', locals())

    def post(self, request):
        user = MessageForm(request.POST)
        if user.is_valid():
            print user.cleaned_data
            Messsge(**user.cleaned_data).save()
            return redirect(reverse('one:main'))
        else:
            return render(request, 'message.html', locals())

#!/usr/bin/python
# -*- coding:utf-8 -*-
from django import forms


class MessageForm(forms.Form):
    username = forms.CharField(required=True, max_length=30, min_length=3, error_messages={
        'required': '该字符安必填', 'max_length': '长度大于30', 'min_length': '长度小于3'
    })
    email = forms.EmailField(required=True, error_messages={
        'required': '该字符安必填'
    })
    address = forms.CharField(required=True, max_length=50, min_length=3, error_messages={
        'required': '该字符安必填', 'max_length': '长度大于50', 'min_length': '长度小于3'
    })
    message = forms.CharField(required=True, max_length=100, min_length=3, error_messages={
        'required': '该字符安必填', 'max_length': '长度大于100', 'min_length': '长度小于3'
    })

#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Insert your description
"""

from django import forms
from students.models import Student


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


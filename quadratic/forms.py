# -*- coding: utf-8 -*-
from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(required=True, label = "коэффициент a")
    b = forms.IntegerField(required=True, label = "коэффициент b")
    c = forms.IntegerField(required=True, label = "коэффициент c")

    def clean_a(self):
        a = self.cleaned_data['a']

        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")

        return a

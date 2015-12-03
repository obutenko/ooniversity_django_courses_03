# -*- coding: utf-8 -*- 
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms
from forms import QuadraticForm

def eq_diction(temp, item):

    eq_dict = {key+'_unit':'коэффициент не целое число' for key,value in item.items() if not value.strip('-').isdigit()}
    eq_dict.update({key:item[key] if key in item else '' for key in temp})
    eq_dict.update({key+'_unit': 'коэффициент не определен' for key in temp if eq_dict[key] == ''})
    eq_dict.update({key+'_unit': False for key in temp if key+'_unit' not in eq_dict})    
    eq_dict['a_unit'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю' if eq_dict['a'] == '0' else eq_dict['a_unit']
    return eq_dict

def roots_eq(temp):
    a, b, c = temp
    eq_dict = {}
    a = float(a)
    b = float(b)
    c = float(c)
    dsc = discr = b**2 - 4 * a * c;
    eq_dict['dsc'] = int(dsc)
    if dsc < 0:
        eq_dict['dsc_unit'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    elif dsc == 0:
        x = -b / (2 * a)
        eq_dict['dsc_unit'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
    else:
        x1 = (-b + dsc ** (1/2.0)) / (2*a)
        x2 = (-b - dsc ** (1/2.0)) / (2*a)
        eq_dict['dsc_unit'] = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)

    return eq_dict

def quadratic_results(request):
    form = QuadraticForm()
    dsc, keys = True, ('a','b','c')
    eq_dict = eq_diction(keys, request.GET)
    for i in keys:
        if eq_dict[i +'_unit']:
            dsc = False
            break
    if dsc:
        eq_dict.update(roots_eq((eq_dict['a'], eq_dict['b'], eq_dict['c'])))
        eq_dict['discr'] = True
    else:
        eq_dict['discr'] = False
    eq_dict['form'] = form
    return render_to_response('quadratic/results.html', eq_dict)



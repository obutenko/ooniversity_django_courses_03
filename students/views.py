# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from students.models import Student, CourseApplication
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages
from students.forms import StudentModelForm

def create(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = u'Student {} {} has been successfully added.' .format(application.surname, application.name)
			messages.success(request, mess)
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, u'Info on the student has been sucessfully changed.')
	else:
		form = StudentModelForm(instance=application)
	return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
		application.delete()
		mess = u'Info on {} {} has been sucessfully deleted.' .format(application.name, application.surname)
		messages.success(request, mess)
		return redirect('students:list_view')
    return render(request, 'students/remove.html', {'full_name': application.name+ ' ' +application.surname}) 








class StudentApplyForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	package = forms.ChoiceField(choices=(
		('standart', 'Standart'),
		('gold', 'Gold'),
		('vip', 'VIP')),
		widget=forms.RadioSelect)
	subscribe = forms.BooleanField(required=False)


class CourseApplicationForm(forms.ModelForm):
	class Meta:
		model = CourseApplication
		exclude = ['comment', 'is_active']
		widgets = {'package': forms.RadioSelect}

def list_view(request):
	if request.GET.get('course_id'):
		stud = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		stud = Student.objects.all()
	#print Student.courses.all()
	#lesn = Lesson.objects.filter(course=course_id)
	return render(request, 'students/list.html', {'students': stud})

def detail(request, detail_id):
	#stud = Student.objects.get(id = detail_id)
	
	#cour = Course.objects.get(id=course_id)
	#lesn = Lesson.objects.filter(course=course_id)
	return render(request, 'students/detail.html', {'student': Student.objects.get(id = detail_id)})

def apply_to_course(request):
	if request.method == 'POST':
		form = CourseApplicationForm(request.POST)
		if form.is_valid():
			application = form.save()
			'''
			data = form.cleaned_data
			application = CourseApplication()
			application.name = data['name']
			application.email = data['email']
			application.package = data['package']
			application.subscribe = data['subscribe']
			course = Course.objects.get(id=1)
			application.course = course
			application.save()
			'''			
			messages.success(request, 'Form saved!!!')
			return redirect('students:apply')
	else:
		form = CourseApplicationForm(initial={'subscribe': True, 'package': 'gold'})
	return render(request, 'students/apply.html', {'form': form})


def edit_application(request, pk):
	application = CourseApplication.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseApplicationForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, 'Form saved!!!')
			return redirect('students:apply')
	else:
		form = CourseApplicationForm(instance=application)
	return render(request, 'students/edit_application.html', {'form': form})


def delete_application(request, pk):
	application = CourseApplication.objects.get(id=pk)
	if request.method == 'POST':
		application.delete()
		messages.success(request, 'Object deleted!!!')
		return redirect('students:apply')
	return render(request, 'students/delete_application.html')




# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, pk):
    return render(request, 'courses/detail.html', {'course' : Course.objects.get(id=pk)})


def add(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = 'Course {} has been successfully added.'.format(application.name)
			messages.success(request, mess)
			return redirect('index')
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html', {'form': form})

def add_lesson(request, pk):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = 'Lesson {} has been successfully added.'.format(application.subject)
			messages.success(request, mess)
			return redirect('courses:detail', application.course.id)
	else:
		form = LessonModelForm()
	return render(request, 'courses/add_lesson.html', {'form': form})


def edit(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, 'The changes have been saved.')
			return redirect('courses:edit',  application.id)
	else:
		form = CourseModelForm(instance=application)
	return render(request, 'courses/edit.html', {'form': form})

def remove(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
		application.delete()
		mess = 'Course {} has been deleted.'.format(application.name)
		messages.success(request, mess)
		return redirect('index')
    return render(request, 'courses/remove.html', {'name': application.name})


"""
class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course
"""
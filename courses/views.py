#-*-coding: utf-8-*-
from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
import models
from forms import *
#import pybursa.utils

def view_item(request, obj_id, obj_class):
    class_name = obj_class.__name__.lower()
    obj = get_object_or_404(obj_class, id=obj_id)
    return render(request, '%ss/detail.html' % class_name, {class_name: obj, 'id': obj_id})

def detail(request, course_id):
   return view_item(request, course_id, Course)

# def detail(request,course_id):
#     course =  get_object_or_404(Course, pk=course_id)
#     return render(request, 'detail.html', {'course': course, 'id': str(course.id)})

def add(request):
    if request.POST:
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Course " + form.cleaned_data['name'] + " has been successfully added."
            messages.success(request, text)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):
    cd = Course.objects.get(id=course_id)
    form = CourseModelForm(instance=cd)
    if request.POST:
        form = CourseModelForm(request.POST, instance=cd)
        if form.is_valid():
            form.save()
            text = "The changes have been saved."
            messages.success(request, text)
            return redirect('courses:edit', course_id=course_id)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, course_id):
    cd = Course.objects.get(id=course_id)
    if request.POST:
        text = "Course {0} has been deleted.".format(str(cd))
        messages.success(request, text)
        cd.delete()
        return redirect('index')
    return render(request, 'courses/remove.html', {'cd':cd})

def add_lesson(request, course_id):
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            less = form.save()
            text = "Lesson {0} has been successfully added.".format(form.cleaned_data['subject'])
            messages.success(request, text)
            return redirect('courses:detail', less.course.id)
    else:
        cd = Course.objects.get(id=course_id)
        form = LessonModelForm(initial={'course': cd})
    return render(request, 'courses/add_lesson.html', {'form': form})

from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

# Create your views here.

def detail (request, course_id):
       cd = Course.objects.get(id=course_id)
       ll = Lesson.objects.filter(course=course_id) 
       return render (request, 'courses/detail.html',  {'course_detail': cd, 'lessons_list': ll})

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
            return redirect('courses:edit', course_id)
    return render(request, 'courses/edit.html', {'form': form})    

def remove(request, course_id):
    cd = Course.objects.get(id=course_id)
    if request.POST:
        text = "Course " + cd.name + " has been deleted."
        messages.success(request, text)  
        cd.delete()
        return redirect('index')
    return render(request, 'courses/remove.html', {'cd': cd})    


# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"

    def get_context_data(self, **kwargs):
        pk = self.object.pk
        courses = Course.objects.get(id=pk)
        lessons = courses.lesson_set.all()
        coaches = courses.coach.user.get_full_name()
        assistants = courses.assistant.user.get_full_name()
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['course_id' ] = pk
        context['courses' ] = courses
        context['lessons' ] = lessons
        context['coach' ] = coaches
        context['assistent' ] = assistants
        return context

        
class CourseCreateView(CreateView):
    model = Course
    template_name = "courses/add.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title' ] = "Course creation"
        return context
    
    def form_valid(self, form):
        course_name = self.request.POST
        messages.add_message(self.request, messages.INFO, 
                             'Course %s has been successfully added.' % course_name['name'] )
        return super(CourseCreateView, self).form_valid(form)
        
        
class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/edit.html"
   
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title' ] = "Course update"
        return context

    def form_valid(self, form): 
        messages.add_message(self.request, messages.INFO, 'The changes have been saved')
        return super(CourseUpdateView, self).form_valid(form)
        
    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('courses:edit', kwargs={'pk': pk})
        
class CourseDeleteView(DeleteView):
    model = Course
    template_name = "courses/remove.html"
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, 'Данные удалены')
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)
    

def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            course_subject  = data['subject']
            add_message = 'Course %s has been successfully added.' % course_subject
            new_lesson = LessonModelForm(request.POST)
            result = new_lesson.save()
            messages.success(request, add_message)
            return redirect('/courses/%i' % int(course_id))

    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})

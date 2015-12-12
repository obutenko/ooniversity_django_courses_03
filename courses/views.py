from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        course = self.get_object()
        lesson = course.lesson_set.all()
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lesson'] = lesson
        return context


#def detail(request, course_id):
#    course = Course.objects.get(id=course_id)
#    lesson = course.lesson_set.all()
#    return render(request, 'courses/detail.html', {'course': course, 'lesson': lesson})


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, u'Course %s has been successfully added.' % course.name)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        messages.success(self.request, u'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data()
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, u'Course %s has been deleted.' % course.name)
        return super(CourseDeleteView, self).delete(self, request, *args, **kwargs)


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            messages.success(request, u'Lesson %s has been successfully added.' % new_lesson.subject)
            return redirect('courses:detail', course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})

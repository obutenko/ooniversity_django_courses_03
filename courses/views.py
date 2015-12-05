from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from courses.models import Course, Lesson
from coaches.models import Coach


# Create your views here.
#def index_courses(request):
    #courses_list = Course.objects.all()
    #context = {'courses_list': courses_list}
    #return render(request, 'index.html', context)
    #return render(request, 'index.html', {'courses_list': Course.objects.all()})

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the related Lessons
        #context['lessons_list'] = Lesson.objects.all()
        #Lessons filtered by course_id received in URL
        context['lessons_list'] = Lesson.objects.filter(course_id=self.kwargs.get(self.pk_url_kwarg, None))
        ##context['lessons_list'] = Lesson.objects.filter(course_id=self.kwargs['pk'])
        #Coaches filtered by course_id received in URL
        #context['coaches_list'] = Coach.objects.all()
        context['coaches_list'] = Coach.objects.filter(coach_courses=self.kwargs.get(self.pk_url_kwarg, None))
        ##context['coaches_list'] = Coach.objects.filter(coach_courses=self.kwargs['pk'])
        context['assistants_list'] = Coach.objects.filter(assistant_courses=self.kwargs.get(self.pk_url_kwarg, None))
        ##context['assistant_list'] = Coach.objects.filter(assistant_courses=self.kwargs['pk'])
        return context



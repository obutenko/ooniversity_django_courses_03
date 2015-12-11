from django.shortcuts import render, redirect
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    template_name = 'feedback.html'
    model = Feedback
    success_url = reverse_lazy('feedback.html')
    
    def form_valid(self, form):
        feedback = form.save()
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        mail_admins(feedback.subject, feedback.message)
        return super(FeedbackView, self).form_valid(form) 

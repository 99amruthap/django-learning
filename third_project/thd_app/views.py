from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
# Create your class based views here.



# def index(request):
#     return render(request,'index.html')

# OOP based views

# class CBView(View):
#     def get(self, request):
#         return HttpResponse('hello i am here')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'I am Injected Here'
        return context

class SchoolListView(ListView):
    #  out own context name for School class
    # context_object_name = 'school'
    model = models.School
    template_name = 'school_list.html'
#      it returns the name school_list for School class

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'school_detail.html'

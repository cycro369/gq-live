from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .filters import cardFilter
from .models import *
from django.db.models import Avg


def index(request):

	return render(request,'card/index.html')


def search_lrn(request):

	try:	
		search = request.POST.get('search')

		Student_query = Student.objects.filter(LRN=search)
		grade_query = Card.objects.filter(Student_LRN=search)

		context = {'Student_query':Student_query, 'grade_query': grade_query,}

	except Student.DoesNotExist:

		raise Http404("LRN Does not Exist")

	return render(request,'card/search.html', context)
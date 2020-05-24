import django_filters

from .models import *

class cardFilter(django_filters.FilterSet):

	class Meta: 
		model: Card 
		fieds = {'LRN': ['exact'],
		'Level': ['exact'],
		'Section': ['exact'],}
from django.contrib import admin
from .models import Card, Level, Student

# Register your models here.

admin.site.site_header = "Grade Query Admin"

#admin panel


class LevelSectionAdmin(admin.ModelAdmin):

	list_display = ('Grade','Section',)

admin.site.register(Level, LevelSectionAdmin)


class SubjectAdmin(admin.ModelAdmin):

	search_fields = ('Student_LRN',)
	list_display = ('Student_LRN','Filipino','English',
		'Mathematics','Science','AP','ESP',
		'TLE','MAPEH','GenAvg','Status')

	list_filter = ('Levels',)
	autocomplete_fields = ('Student_LRN',)

admin.site.register(Card, SubjectAdmin)

class  StudentAdmin(admin.ModelAdmin):

	search_fields = ('Name','LRN')
	list_display = ('LRN','Name','Levels')
	list_filter = ('Levels',)

admin.site.register(Student,StudentAdmin)


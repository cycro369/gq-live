

from django.db import models

# Create your models here.


class Level(models.Model):
    GRADE = (('7','7')),(('8','8')),(('9','9')),(('10','10'))

    Grade = models.CharField(max_length=200, null=True, choices=GRADE)
    Section = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural="Grade and Sections"

    @property
    def levelsection(self):
        return '%s %s' % (self.Grade, self.Section)

    def __str__(self):
        return self.levelsection
    


class Student(models.Model):

    GRADE = (('7','7')),(('8','8')),(('9','9')),(('10','10'))

    LRN = models.CharField(max_length=200, primary_key=True, null= False)
    Name = models.CharField(max_length=200, null= True)
    Levels = models.ForeignKey(Level, on_delete = models.CASCADE)


    class Meta:
        verbose_name_plural='Student Lists'


    @property
    def get_combo(self): 
       	return self.Name

    def __str__(self):
    	return self.get_combo


class Card(models.Model):

    STATUS = (('RETAINED','RETAINED')),(('PROMOTED','PROMOTED'))
    
    Student_LRN = models.ForeignKey(Student,  on_delete=models.CASCADE)
    Levels = models.ForeignKey(Level, on_delete = models.CASCADE)
    Filipino = models.CharField(max_length=200, null= True)
    English = models.CharField(max_length=200, null= True)
    Mathematics = models.CharField(max_length=200, null= True)
    Science = models.CharField(max_length=200, null= True)
    AP = models.CharField(max_length=200, null= True)
    ESP = models.CharField(max_length=200, null= True)
    TLE = models.CharField(max_length=200, null= True)
    MAPEH = models.CharField(max_length=200, null= True)
    GenAvg = models.CharField(max_length=200, null=True)
    Status = models.CharField(max_length=200, null= True, choices= STATUS)


    class Meta:
        verbose_name_plural='Student Grades'
        ordering =('-Student_LRN',)

    def __str__(self):
        return '{}'.format(self.Student_LRN)


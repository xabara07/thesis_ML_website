from .models import Data, student
from django.db import models

# return all students from student table
students = student.objects.all()

# return first student in table
student1 = student.objects.first()

# return last student in table
student1 = student.objects.last()

# return single student by firstname
student1 = student.objects.get(firstname= "Joylyn")

# return single student by firstnam
student1= student.objects.get(id=1)

data1 = student1.data_set.all() #return student1 all data

data = Data.objects.last() # return last data in table

print(data.students.firstname) # return student lastname in the data

datas = Data.objects.filter() 

datas = Data.objects.filter(course=3) # return data from datas table with certain filtered value

# Datas sort objects by id
datas = Data.objects.all().order_by('id') #L2G
datas = Data.objects.all().order_by('-id') #G2L

csdata = student1.data_set.filter(course=3).count() # return student1 total count for number of time a "CS" was chosen

allDatas = {}
for studata in student1.data_set.all():
    if studata.students.studentID in allDatas:
        allDatas[studata.students.studentID] += 1
    else:
        allDatas[studata.students.studentID] = 1


class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
parent.childmodel_set.all()

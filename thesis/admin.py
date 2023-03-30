from django.contrib import admin
from .models import Data, student

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('studentId', 'age', 'sex', 'course', 'year', 'status', 'personality', 'wstud', 'scholar', 
                    'TM3', 'TM4', 'TM5', 'TM6', 'TM7',
                    'CAP2', 'CAP3', 'CAP4', 
                    'GSS1', 'GSS2', 'GSS3', 'GSS4','GSS5', 'GSS6', 'GSS7', 
                    'EP1', 'EP2', 'EP3', 'EP5', 
                    'NT1', 'NT2', 'NT3',
                    'desktop', 'laptop', 'mobile', 
                    'wifi', 'c_data',
                    'h_speed', 'l_speed', 
                    'predictions', 'datePredicted') 


admin.site.register(Data, DataAdmin)

class DataStud(admin.ModelAdmin):
    list_display = ('studentID', 'firstname', 'lastname', 'stud_course', 'stud_year', 'stud_age', 'stud_sex', 'phone', 'date_created')


admin.site.register(student, DataStud)

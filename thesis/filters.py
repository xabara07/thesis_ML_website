import django_filters
from django_filters import CharFilter
from .models import *

class PredictFilter(django_filters.FilterSet):
    predictions = CharFilter(field_name='predictions', lookup_expr='icontains')
    class Meta:
        model = Data
        fields = ['students', 'studentId', 'sex', 'course', 'year',
                'personality', 'predictions']

class StudFilter(django_filters.FilterSet):
    firstname = CharFilter(field_name='firstname', lookup_expr='icontains')
    lastname = CharFilter(field_name='lastname', lookup_expr='icontains')
    class Meta:
        model = student
        fields = ['studentID', 'firstname', 'lastname', 'stud_sex', 'stud_course', 'stud_year']
            
        

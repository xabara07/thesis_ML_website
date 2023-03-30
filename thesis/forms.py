from dataclasses import fields
from tkinter import Label
from django import forms
from django.forms.widgets import ClearableFileInput
from  .models import Data, student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['students', 'studentId', 'age', 'sex', 'course', 'year',
                'status', 'scholar', 'wstud', 'personality',
                'TM3', 'TM4', 'TM5', 'TM6', 'TM7',
                'CAP2', 'CAP3', 'CAP4',
                'GSS1', 'GSS2', 'GSS3', 'GSS4', 'GSS5', 'GSS6', 'GSS7',
                'EP1', 'EP2', 'EP3', 'EP5',
                'NT1', 'NT2', 'NT3',
                'desktop', 'laptop', 'mobile',
                'wifi', 'c_data',
                'h_speed', 'l_speed']

        widgets = {
            'students': forms.TextInput(attrs={'readonly': True})
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomClearableFileInput(ClearableFileInput):
    template_name = 'custom_clearable_file_input.html'

class studentForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=CustomClearableFileInput)
    class Meta:
        model = student
        fields = '__all__'
        exclude = ['user', 'email']


class GPAForm(forms.Form):
    grade1 = forms.FloatField(label="Subject Grade 1")
    units1 = forms.IntegerField()

    grade2 = forms.FloatField(label="Subject Grade 2")
    units2 = forms.IntegerField()

    grade3 = forms.FloatField(label="Subject Grade 3")
    units3 = forms.IntegerField()

    grade4 = forms.FloatField(label="Subject Grade 4")
    units4 = forms.IntegerField()

    grade5 = forms.FloatField(label="Subject Grade 5")
    units5 = forms.FloatField()

    grade6 = forms.FloatField(label="Subject Grade 6")
    units6 = forms.IntegerField()

    grade7 = forms.FloatField(label="Subject Grade 7")
    units7 = forms.IntegerField()

    grade8 = forms.FloatField(label="Subject Grade 8")
    units8 = forms.IntegerField()

    grade9 = forms.FloatField(label="Subject Grade 9")
    units9 = forms.IntegerField()

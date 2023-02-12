from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from sklearn.ensemble import BaggingRegressor
from django.contrib.auth.models import User
import joblib
# import pickle
# import pandas as pd


# Create your models here.
SEX = (
    (0, 'Female'),
    (1, 'Male')
)

COURSE = (
    (1, 'BS Community Development'),
    (2, 'BS Information Technology'),
    (3, 'BS Computer Science'),
    (4, 'BS Social Work')
)

COURSE2 = (
    ('BSCD', 'BS Community Development'),
    ('BSIT', 'BS Information Technology'),
    ('BSCS', 'BS Computer Science'),
    ('BSSW', 'BS Social Work')
)

YR_LEVEL = (
    (2, '2nd Year'),
    (3, '3rd Year'),
    (4, '4th Year')
)

STATUS = (
    (1, 'Low (₱9,520-₱19,040)'),
    (2, 'Low Middle (₱19,040-₱38,080)'),
    (3, 'Middle (₱38,080-₱66,640)'),
    (4, 'Upper Middle (₱66,640-₱114,240)'),
    (5, 'Upper but not rich (₱114,240-₱190,400)'),
    (6, 'Rich (At least ₱190,400)')
)

SUPPORT = (
    (0, 'NO'),
    (1, 'YES')
)

SCHOLAR = (
    (0, 'NO'),
    (1, 'YES')
)

WORKING = (
    (0, 'NO'),
    (1, 'YES')
)

PERSONALITY = (
    (0, 'ISTJ'),
    (1, 'ESFJ'),
    (2, 'ENTP'),
    (3, 'ISFJ'),
    (4, 'ENFJ'),
    (5, 'INFJ'),
    (6, 'ISFP'),
    (7, 'INTJ'),
    (8, 'ENTJ'),
    (9, 'ESTP'),
    (10, 'INFP'),
    (11, 'ESFP'),
    (12, 'ESTJ'),
    (13, 'ENFP'),
    (14, 'ISTP'),
    (15, 'INTP')
)
#Time Management
TM_1 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
TM_2 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
TM_3 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
TM_4 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
TM_5 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
TM_6 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
TM_7 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

#Class Attendance Participation
CAP_1 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
CAP_2 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
CAP_3 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
CAP_4 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

#General Study Stratery
GSS_1 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
GSS_2 =  (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
GSS_3 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
GSS_4 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
GSS_4 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
GSS_5 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
GSS_6 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
GSS_7 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

#Exam Preparation
EP_1 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
EP_2 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
EP_3 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
EP_4 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
EP_5 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

EP_6 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

#Note Taking
NT_1 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
NT_2 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
NT_3 = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

#Digital Resourses
DESKTOPS = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
LAPTOPS = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
MOBILEPHONE = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
TABLETS = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

WI_FI = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
PRE_WIFI = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
CELL_DATA = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
TET_HOTSPPOT = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

VERYHIGH = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
HIGH = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
MODERATE = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)
LIGHT = (
    (1, 'Always'),
    (2, 'Sometimes'),
    (3, 'Never')
)

ID = (
    ('1st Sem', '1st Sem'),
    ('2nd Sem', '2nd Sem')
)

#----------------------------------------------------------------------------------------------------

class student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    studentID = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    stud_course = models.PositiveBigIntegerField(choices=COURSE, null=True, verbose_name=u"Course")
    stud_year = models.PositiveBigIntegerField(choices=YR_LEVEL, null=True, verbose_name=u"Year")
    stud_age = models.PositiveBigIntegerField(validators = [MinValueValidator(17), MaxValueValidator(40)],null=True, verbose_name=u"Age")
    stud_sex = models.PositiveBigIntegerField(choices=SEX, null=True, verbose_name=u"Sex")
    phone = models.PositiveBigIntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(default="unknown.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.firstname

class Data(models.Model):
    students = models.ForeignKey(student, null=True, on_delete=models.SET_NULL, verbose_name=u"Student's No.")
    #Personal
    studentId = models.CharField(max_length=100, choices=ID, null=True, verbose_name=u"Semester")
    age = models.PositiveBigIntegerField(validators = [MinValueValidator(17), MaxValueValidator(40)],null=True)
    sex = models.PositiveBigIntegerField(choices=SEX, null=True)
    course = models.PositiveBigIntegerField(choices=COURSE, null=True)
    year = models.PositiveBigIntegerField(choices=YR_LEVEL, null=True)

    #Demographic
    status = models.PositiveBigIntegerField(choices=STATUS, null=True, verbose_name=u"Socio-Economic Status")
    # support = models.PositiveBigIntegerField(choices=SUPPORT, null=True, verbose_name=u"Family Support?")
    scholar = models.PositiveBigIntegerField(choices=SCHOLAR, null=True, verbose_name=u"Are you a Scholar?")
    wstud = models.PositiveBigIntegerField(choices=WORKING, null=True, verbose_name=u"Are you a working student?")
    personality = models.PositiveBigIntegerField(choices=PERSONALITY,null=True, verbose_name=u"Personality Type")

    #Study Habits
    # TM1 = models.PositiveBigIntegerField(choices=TM_1, null=True, verbose_name=u"TM1: I have a study schedule with times set aside to study each subject.")
    # TM2 = models.PositiveBigIntegerField(choices=TM_2, null=True, verbose_name=u"TM2: I use my free time between classes for reading or reviewing.")
    TM3 = models.PositiveBigIntegerField(choices=TM_3, null=True, verbose_name=u"TM3: I balance my study time with recreation and leisure time.")
    TM4 = models.PositiveBigIntegerField(choices=TM_4, null=True, verbose_name=u"TM4: I have a calendar of the semester and it is marked with exam dates, project due dates and assignments.")
    TM5 = models.PositiveBigIntegerField(choices=TM_5, null=True, verbose_name=u"TM5: I keep a weekly schedule of my classes and activities.")
    TM6 = models.PositiveBigIntegerField(choices=TM_6, null=True, verbose_name=u"TM6: I use daily “to do” lists.")
    TM7 = models.PositiveBigIntegerField(choices=TM_7, null=True, verbose_name=u"TM7: I study on the weekends.")
    
    # CAP1 = models.PositiveBigIntegerField(choices=CAP_1, null=True, verbose_name=u"CAP1: I attend class regularly.")
    CAP2 = models.PositiveBigIntegerField(choices=CAP_2, null=True, verbose_name=u"CAP2: I get to class early or on time.")
    CAP3 = models.PositiveBigIntegerField(choices=CAP_3, null=True, verbose_name=u"CAP3: I come to class prepared, having completed the reading.")
    CAP4 = models.PositiveBigIntegerField(choices=CAP_4, null=True, verbose_name=u"CAP4: I always find a comfortable place for me when I’m listening to the lecture or watching lecture’s video.")

    GSS1 = models.PositiveBigIntegerField(choices=GSS_1, null=True, verbose_name=u"GSS1: I plan sufficient time to get assignments done.")
    GSS2 = models.PositiveBigIntegerField(choices=GSS_2, null=True, verbose_name=u"GSS2: I turn in all assignments on time.")
    GSS3 = models.PositiveBigIntegerField(choices=GSS_3, null=True, verbose_name=u"GSS3: I use index cards to write down important information and then review that information when I am “waiting” around.")
    GSS4 = models.PositiveBigIntegerField(choices=GSS_4, null=True, verbose_name=u"GSS4: I work on more difficult task first.")
    GSS5 = models.PositiveBigIntegerField(choices=GSS_5, null=True, verbose_name=u"GSS5: I set specific goals for each subject.")
    GSS6 = models.PositiveBigIntegerField(choices=GSS_6, null=True, verbose_name=u"GSS6: I have a regular study area that is free of distractions.")
    GSS7 = models.PositiveBigIntegerField(choices=GSS_7, null=True, verbose_name=u"GSS7: I take breaks when I study.")

    EP1 = models.PositiveBigIntegerField(choices=EP_1, null=True, verbose_name=u"EP1: I review older material first when studying for exams.")
    EP2 = models.PositiveBigIntegerField(choices=EP_2, null=True, verbose_name=u"EP2: When studying for exams, I review over several chapter.")
    EP3 = models.PositiveBigIntegerField(choices=EP_3, null=True, verbose_name=u"EP3: I study for exams at least five days in advance.")
    # EP4 = models.PositiveBigIntegerField(choices=EP_4, null=True, verbose_name=u"EP4: I make up exam questions and answer them as I study")
    EP5 = models.PositiveBigIntegerField(choices=EP_5, null=True, verbose_name=u"EP5: I make up exam questions using the same format that the actual exam will use.")
    # EP6 = models.PositiveBigIntegerField(choices=EP_6, null=True, verbose_name=u"EP6: I review for exams with a peer or a small study group.")

    NT1 = models.PositiveBigIntegerField(choices=NT_1, null=True, verbose_name=u"NT1: I take organized and legible notes during class.")
    NT2 = models.PositiveBigIntegerField(choices=NT_2, null=True, verbose_name=u"NT2: I review and revise my notes soon after class.")
    NT3 = models.PositiveBigIntegerField(choices=NT_3, null=True, verbose_name=u"NT3: I take notes as I read my assignments.")

    #Digital Resources
    desktop = models.PositiveBigIntegerField(choices=DESKTOPS, null=True, verbose_name=u"How often do you use Desktop for academic purposes?")
    laptop = models.PositiveBigIntegerField(choices=LAPTOPS, null=True, verbose_name=u"How often do you use Laptop for academic purposes")
    mobile = models.PositiveBigIntegerField(choices=MOBILEPHONE, null=True, verbose_name=u"How often do you use Mobile Phone for academic purposes")
    # tablet = models.PositiveBigIntegerField(choices=TABLETS, null=True, verbose_name=u"How often do you use Tablet for academic purposes")

    wifi = models.PositiveBigIntegerField(choices=WI_FI, null=True, verbose_name=u"How often do you use WiFi for internet connectivity?")
    # p_wifi = models.PositiveBigIntegerField(choices=PRE_WIFI, null=True, verbose_name=u"Prepaid Wi-Fi")
    c_data = models.PositiveBigIntegerField(choices=CELL_DATA, null=True, verbose_name=u"How often do you use Cellular Data for internet connectivity?")
    # hotspot = models.PositiveBigIntegerField(choices=TET_HOTSPPOT, null=True, verbose_name=u"Hotspot Tethering")

    # vh_speed = models.PositiveBigIntegerField(choices=VERYHIGH, null=True, verbose_name=u"Very High")
    h_speed = models.PositiveBigIntegerField(choices=HIGH, null=True, verbose_name=u"Does your internet connection frequently in high speed?")
    # m_speed = models.PositiveBigIntegerField(choices=MODERATE, null=True, verbose_name=u"Moderate")
    l_speed = models.PositiveBigIntegerField(choices=LIGHT, null=True, verbose_name=u"Does your internet connection frequently in light speed?")

    #Grade
    # gpa = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]  , null=True)

    predictions = models.CharField(max_length=20, blank=True)
    

    def calculate_TM(self):
        return(self.TM3 + self.TM4 + self.TM5 + self.TM6 + self.TM7) / 15 * 100
    
    def save(self, *args, **kwargs):
        # Unpickle model
        ml_model = joblib.load('thesis_Model_Final.pkl')
        self.predictions = ml_model.predict(
            [[self.age, self.sex, self.course, self.year, 
            self.status, self.scholar, self.wstud, self.personality, 
            self.TM3, self.TM4, self.TM5, self.TM6, self.TM7, 
            self.CAP2, self.CAP3, self.CAP4, 
            self.GSS1, self.GSS2, self.GSS3, self.GSS4, self.GSS5, self.GSS6, self.GSS7, 
            self.EP1, self.EP2, self.EP3, self.EP5, 
            self.NT1, self.NT2, self.NT3, 
            self.desktop, self.laptop, self.mobile,
            self.wifi, self.c_data, 
            self.h_speed, self.l_speed]])
        self.predictions = ' '.join(map(str, self.predictions))
        self.predictions = self.predictions.replace('[','').replace(']','')
        return super().save(*args, *kwargs)

    def __str__(self):
        return self.studentId



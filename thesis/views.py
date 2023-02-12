from tkinter.tix import INTEGER
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Data, student
from .forms import DataForm, CreateUserForm, studentForm, GPAForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorations import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .filters import PredictFilter, StudFilter
import math

# import datetime
# from django.template.loader import render_to_string
# from weasyprint import HTML
# HTML('https://weasyprint.org/').write_pdf('/tmp/weasyprint-website.pdf')
# import tempfile


# accounts
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for ' + username)
                return redirect('login')

        context = {'form':form}
        return render(request, "accounts/register.html", context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Log-in Success!")
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect!')

    context = {}
    return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Log-out Success!")
    return redirect('login')

#--------------
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render({}, request))


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def personality(request: HttpRequest) -> HttpResponse:
    return render(request, "personality.html")
    

@login_required(login_url='login') # make page visible when logged-in
def predict(request):
    final = 0
    students = request.user.student
    year = request.user.student.stud_year
    course = request.user.student.stud_course
    age = request.user.student.stud_age
    sex = request.user.student.stud_sex

    form = DataForm(initial={'students':students, 'year':year, 'course':course, 'age':age, 'sex':sex})
    
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            prediction = form.save()
            final = (prediction.pk)
            return redirect('result', pk=prediction.pk)
        
    # else:
    #     form = DataForm()

    context = {
        'form': form, 'final':final
    }
    return render(request, "predict.html", context)
    

@login_required(login_url='login') # make page visible when logged-in
@admin_only
def predictions(request):
    male_no = student.objects.filter(stud_sex=1).count()
    male_no = int(male_no)
    print('Number of Male Are',male_no)

    female_no = student.objects.filter(stud_sex=0).count()
    female_no = int(female_no)
    print('Number of Female Are',female_no)

    gender_list = ['Female','Male']
    gender_number = [female_no, male_no]


    predicted_acads = Data.objects.all()
    students = student.objects.all()

    myFilter = PredictFilter(request.GET, queryset=predicted_acads)
    predicted_acads = myFilter.qs

    studFilter = StudFilter(request.GET, queryset=students)
    students = studFilter.qs

    total_students = students.count()
    total_datas = predicted_acads.count()

    context = {
        'predicted_acads': predicted_acads,
        'students': students,
        'total_students': total_students,
        'total_datas': total_datas,
        'myFilter': myFilter,
        'studFilter':studFilter,
        'gender_list':gender_list, 'gender_number':gender_number
    }
    return render(request, "predictions.html", context)

def data(request, pk):
    data = Data.objects.get(id=pk)

    context = {
        'data': data
        }
    return render(request, "data.html", context)


def result(request, pk):
    predicted_acads = Data.objects.get(id=pk)
    # predicted_acads = Data.objects.all()
    # predicted_acads = request.user.student.data_set.all()
    # TIME MANAGEMENT 
    if predicted_acads.TM4 == 1:
        predicted_acads.TM4 = 3
    elif predicted_acads.TM4 == 3:
        predicted_acads.TM4 = 1
        
    if predicted_acads.TM5 == 1:
        predicted_acads.TM5 = 3
    elif predicted_acads.TM5 == 3:
        predicted_acads.TM5 = 1

    if predicted_acads.TM6 == 1:
        predicted_acads.TM6 = 3
    elif predicted_acads.TM6 == 3:
        predicted_acads.TM6 = 1

    if predicted_acads.TM3 == 1:
        predicted_acads.TM3 = 3
    elif predicted_acads.TM3 == 3:
        predicted_acads.TM3 = 1

    if predicted_acads.TM7 == 1:
        predicted_acads.TM7 = 3
    elif predicted_acads.TM7 == 3:
        predicted_acads.TM7 = 1

    #Class Attendance and Participation
    if predicted_acads.CAP2 == 1:
        predicted_acads.CAP2 = 3
    elif predicted_acads.CAP2 == 3:
        predicted_acads.CAP2 = 1

    if predicted_acads.CAP3 == 1:
        predicted_acads.CAP3 = 3
    elif predicted_acads.CAP3 == 3:
        predicted_acads.CAP3 = 1

    if predicted_acads.CAP4 == 1:
        predicted_acads.CAP4 = 3
    elif predicted_acads.CAP4 == 3:
        predicted_acads.CAP4 = 1

    #General Study Strategy
    if predicted_acads.GSS1 == 1:
        predicted_acads.GSS1 = 3
    elif predicted_acads.GSS1 == 3:
        predicted_acads.GSS1 = 1
        
    if predicted_acads.GSS2 == 1:
        predicted_acads.GSS2 = 3
    elif predicted_acads.GSS2 == 3:
        predicted_acads.GSS2 = 1

    if predicted_acads.GSS3 == 1:
        predicted_acads.GSS3 = 3
    elif predicted_acads.GSS3 == 3:
        predicted_acads.GSS3 = 1

    if predicted_acads.GSS4 == 1:
        predicted_acads.GSS4 = 3
    elif predicted_acads.GSS4 == 3:
        predicted_acads.GSS4 = 1

    if predicted_acads.GSS5 == 1:
        predicted_acads.GSS5 = 3
    elif predicted_acads.GSS5 == 3:
        predicted_acads.GSS5 = 1

    if predicted_acads.GSS6 == 1:
        predicted_acads.GSS6 = 3
    elif predicted_acads.GSS6 == 3:
        predicted_acads.GSS6 = 1

    if predicted_acads.GSS7 == 1:
        predicted_acads.GSS7 = 3
    elif predicted_acads.GSS7 == 3:
        predicted_acads.GSS7 = 1

    #Exam Preparation
    if predicted_acads.EP1 == 1:
        predicted_acads.EP1 = 3
    elif predicted_acads.EP1 == 3:
        predicted_acads.EP1 = 1

    if predicted_acads.EP2 == 1:
        predicted_acads.EP2 = 3
    elif predicted_acads.EP2 == 3:
        predicted_acads.EP2 = 1

    if predicted_acads.EP3 == 1:
        predicted_acads.EP3 = 3
    elif predicted_acads.EP3 == 3:
        predicted_acads.EP3 = 1

    if predicted_acads.EP5 == 1:
        predicted_acads.EP5 = 3
    elif predicted_acads.EP5 == 3:
        predicted_acads.EP5 = 1

    #Note Taking
    if predicted_acads.NT1 == 1:
        predicted_acads.NT1 = 3
    elif predicted_acads.NT1 == 3:
        predicted_acads.NT1 = 1

    if predicted_acads.NT2 == 1:
        predicted_acads.NT2 = 3
    elif predicted_acads.NT2 == 3:
        predicted_acads.NT2 = 1

    if predicted_acads.NT3 == 1:
        predicted_acads.NT3 = 3
    elif predicted_acads.NT3 == 3:
        predicted_acads.NT3 = 1

    result_tm = (predicted_acads.TM3 + predicted_acads.TM4 + predicted_acads.TM5 + predicted_acads.TM6 + predicted_acads.TM7) / 15 * 100
    result_cap = (predicted_acads.CAP2 + predicted_acads.CAP3 + predicted_acads.CAP4) / 9 * 100   
    result_gss = (predicted_acads.GSS1 + predicted_acads.GSS2 + predicted_acads.GSS3 + predicted_acads.GSS4 + predicted_acads.GSS5 + predicted_acads.GSS6 + predicted_acads.GSS7) / 21 * 100
    result_ep = (predicted_acads.EP1 + predicted_acads.EP2 + predicted_acads.EP3 + predicted_acads.EP5) / 12 * 100
    result_nt = (predicted_acads.NT1 + predicted_acads.NT2 + predicted_acads.NT3) / 9 * 100

    result_list = ['Time Management','Class Attendance and Participation', 'General Study Strategy', 'Exam Preparation', 'Note Taking']
    result_num = [result_tm, result_cap, result_gss, result_ep, result_nt]


    stud = request.user.student

    context = {
        'predicted_acads': predicted_acads, 'stud':stud, 'result_tm':result_tm,
        'result_cap':result_cap, 'result_gss':result_gss, 'result_ep':result_ep, 'result_nt':result_nt,
        'result_list':result_list, 'result_num':result_num
        }
    return render(request, "result.html", context)

def user(request, pk_user):
    students = student.objects.get(id=pk_user)


    datas = students.data_set.all()
    data_count = datas.count()


    context = {
        'students':students,  'data_count':data_count, 'datas':datas
    }
    return render(request, "accounts/user.html", context)

# admin analytics (Charts) side

def analytics(request):
    predicted_acads = Data.objects.all()
    students = student.objects.all()

    # Sex
    male_no = student.objects.filter(stud_sex=1).count()
    male_no = int(male_no)
    female_no = student.objects.filter(stud_sex=0).count()
    female_no = int(female_no)

    gender_list = ['Female','Male']
    gender_number = [female_no, male_no]

    # Scholar
    scholar_yes = Data.objects.filter(scholar=1).count()
    scholar_no = Data.objects.filter(scholar=0).count()


    scholar_list = ['Yes','No']
    scholar_number = [scholar_yes,scholar_no]

    # Year
    year_2 = student.objects.filter(stud_year=2).count()
    year_2 = int(year_2)
    year_3 = student.objects.filter(stud_year=3).count()
    year_3 = int(year_3)
    year_4 = student.objects.filter(stud_year=4).count()
    year_4 = int(year_4)

    year_list = ['2nd Year', '3rd Year', '4th Year']
    year_number = [year_2, year_3,year_4]

    # COURSE
    course1 = student.objects.filter(stud_course=1).count()
    course1 = int(course1)
    course2 = student.objects.filter(stud_course=2).count()
    course2 = int(course2)
    course3 = student.objects.filter(stud_course=3).count()
    course3 = int(course3)
    course4 = student.objects.filter(stud_course=4).count()
    course4 = int(course4)

    course_list = ['BS Community Development', 'BS Information Technology', 'BS Computer Science', 'BS Social Work']
    course_number = [course1, course2, course3,course4]

    # WORKING STUDENT
    work_no = Data.objects.filter(wstud=0).count()
    work_yes = Data.objects.filter(wstud=1).count()

    work_list = ['No','Yes']
    work_number = [work_no, work_yes]

    # FAMILY SUPPORT
    sup_1 = Data.objects.filter(status=1).count()
    sup_2 = Data.objects.filter(status=2).count()
    sup_3 = Data.objects.filter(status=3).count()
    sup_4 = Data.objects.filter(status=4).count()
    sup_5 = Data.objects.filter(status=5).count()
    sup_6 = Data.objects.filter(status=6).count()

    sup_list = ['Low','Low Middle', 'Middle', 'Upper Middle', 'Upper but not rich', 'rich']
    sup_number = [sup_1, sup_2, sup_3, sup_4, sup_4, sup_5, sup_6]

    # PERSONALITY TYPE
    per_1 = Data.objects.filter(personality=0).count()
    per_2 = Data.objects.filter(personality=1).count()
    per_3 = Data.objects.filter(personality=2).count()
    per_4 = Data.objects.filter(personality=3).count()
    per_5 = Data.objects.filter(personality=4).count()
    per_6 = Data.objects.filter(personality=5).count()
    per_7 = Data.objects.filter(personality=6).count()
    per_8 = Data.objects.filter(personality=7).count()
    per_9 = Data.objects.filter(personality=8).count()
    per_10= Data.objects.filter(personality=9).count()
    per_11= Data.objects.filter(personality=10).count()
    per_12= Data.objects.filter(personality=11).count()
    per_13= Data.objects.filter(personality=12).count()
    per_14= Data.objects.filter(personality=13).count()
    per_15= Data.objects.filter(personality=14).count()
    per_16= Data.objects.filter(personality=15).count()

    per_list = ['ISTJ', 'ESFJ', 'ENTP', 'ISFJ', 'ENFJ', 'INFJ', 'ISFP', 'INTJ', 'ENTJ', 'ESTP',  'INFP', 'ESFP', 'ESTJ', 'ENFP', 'ISTP', 'INTP']
    per_number = [per_1, per_2, per_3, per_4, per_5, per_6, per_7, per_8, per_9, per_10, per_11, per_12, per_13, per_14, per_15, per_16]


    total_students = students.count()
    total_datas = predicted_acads.count()
    context = {
        'predicted_acads': predicted_acads,
        'students': students,
        'gender_list':gender_list, 'gender_number':gender_number,
        'scholar_list':scholar_list, 'scholar_number':scholar_number,
        'year_list':year_list, 'year_number':year_number,
        'course_list':course_list, 'course_number':course_number,
        'work_list':work_list, 'work_number':work_number,
        'sup_list':sup_list, 'sup_number':sup_number,
        'total_students':total_students, 'total_datas':total_datas,
        'per_list':per_list, 'per_number':per_number,
    }
    return render(request, "analytics.html", context)

def prediction(request):
    male_no = student.objects.filter(stud_sex=1).count()
    male_no = int(male_no)
    print('Number of Male Are',male_no)

    female_no = student.objects.filter(stud_sex=0).count()
    female_no = int(female_no)
    print('Number of Female Are',female_no)

    gender_list = ['Female','Male']
    gender_number = [female_no, male_no]

    predicted_acads = Data.objects.all()
    total_datas = predicted_acads.count()
    myFilter = PredictFilter(request.GET, queryset=predicted_acads)
    predicted_acads = myFilter.qs
    context = {
        'predicted_acads': predicted_acads,
        'myFilter': myFilter,
        'gender_list':gender_list, 'gender_number':gender_number,
        'total_datas':total_datas
    }
    return render(request, "prediction.html", context)

def students_list(request):
    students = student.objects.all()
    total_students = students.count()

    studFilter = StudFilter(request.GET, queryset=students)
    students = studFilter.qs
    context = {'students':students, 'studFilter':studFilter, 'total_students':total_students}

    return render(request, "students_list.html", context)

# -----------------------------------------------------------------------


def updateData(request, pk):
    datas = Data.objects.get(id=pk)
    form = DataForm(instance=datas)

    if request.method == 'POST':
        form = DataForm(request.POST, instance=datas)
        if form.is_valid():
            form.save()
            return redirect('result', pk=datas.pk)


    context = {'form':form}
    return render(request, "predict.html", context)


def deleteData(request, pk):
    datas = Data.objects.get(id=pk)

    if request.method == "POST":
        datas.delete()
        return redirect('index')
    context = {'item':datas}
    return render(request, "accounts/delete.html", context)


def deleteStud(request, pk):
    stud = student.objects.get(id=pk)

    if request.method == "POST":
        stud.delete() 
        messages.success(request, "Deleted Successfully!")
        return redirect('students_list')
    context = {'item':stud}
    return render(request, "accounts/delete_stud.html", context)


# user's profile
@login_required(login_url='login') # make page visible when logged-in
@allowed_users(allowed_roles=['student'])
def userprofile(request):

    predicted_acads = Data.objects.all()
    predicted_acads = request.user.student.data_set.all()
    stud = request.user.student

    data_cnts = predicted_acads.count()

    context = {'predicted_acads':predicted_acads, 'data_cnts':data_cnts, 'stud':stud}
    return render(request, "accounts/profile.html", context)



@login_required(login_url='login') # make page visible when logged-in
@allowed_users(allowed_roles=['student'])
def edit_profile(request):
    student = request.user.student
    form = studentForm(instance=student)

    if request.method =='POST':
        form = studentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Edit Profile Successfully!")

    context = {'form':form}
    return render(request, "accounts/edit_profile.html", context)
    

def studentProfile(request, pk_user):
    students = student.objects.get(id=pk_user)

    datas = students.data_set.all()
    data_count = datas.count()

    context = { 'students':students, 'datas':datas, 'data_count':data_count}
    return render(request, "accounts/student.html", context)


@login_required(login_url='login') # make page visible when logged-in
def take_pt(request):
    students = student.objects.all()

    context = {'students':students}
    return render(request, "takept.html", context)


# def export_pdf(request):

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition']= 'attachment; filename=Data' + \
#         str(datetime.datetime.now())+'.pdf'

#     response['Content-Transfer-Encoding'] = 'binary'

#     html_string = render_to_string('data/pdf-output.html')

#     html = HTML(string=html_string)
#     result=html.write_pdf()

#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output=open(output.name, 'rb')
#         response.write(output.read())

#     return response



#Personality Type Views
# --TJ--
def ESTJ(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ESTJ.html")

def ISTJ(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ISTJ.html")

def ENTJ(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ENTJ.html")

def INTJ(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/INTJ.html")

# --TP--
def ESTP(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ESTP.html")

def ISTP(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ISTP.html")

def ENTP(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ENTP.html")

def INTP(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/INTP.html")

# --FJ--
def ESFJ(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ESFJ.html")

def ISFJ(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ISFJ.html")

def ENFJ(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ENFJ.html")

def INFJ(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/INFJ.html")

# --FP--

def ESFP(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ESFP.html")

def ISFP(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ISFP.html")

def ENFP(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/ENFP.html")

def INFP(request: HttpRequest) -> HttpResponse:
    return render(request, "personality/INFP.html")
    

#-------------------------------

def calculate_gpa(request):
    if request.method == 'POST':
        form = GPAForm(request.POST)
        if form.is_valid():
            grade1 = form.cleaned_data['grade1']
            units1 = form.cleaned_data['units1']

            grade2 = form.cleaned_data['grade2']
            units2 = form.cleaned_data['units2']

            grade3 = form.cleaned_data['grade3']
            units3 = form.cleaned_data['units3']

            grade3 = form.cleaned_data['grade3']
            units3 = form.cleaned_data['units3']

            grade4 = form.cleaned_data['grade4']
            units4 = form.cleaned_data['units4']
            
            grade5 = form.cleaned_data['grade5']
            units5 = form.cleaned_data['units5']

            grade6 = form.cleaned_data['grade6']
            units6 = form.cleaned_data['units6']

            grade7 = form.cleaned_data['grade7']
            units7 = form.cleaned_data['units7']

            grade8 = form.cleaned_data['grade8']
            units8 = form.cleaned_data['units8']

            grade9 = form.cleaned_data['grade9']
            units9 = form.cleaned_data['units9']

            # ...and so on, for all 9 grades and units
            total_units = units1 + units2 + units3 + units4 + units5 + units6 + units7 + units8 + units9 
            total_points = (grade1 * units1) + (grade2 * units2) + (grade3 * units3) + (grade4 * units4) + (grade5 * units5) + (grade6 * units6) + (grade7 * units7) + (grade8 * units8) + (grade9 * units9)
            gpa = total_points / total_units
            return render(request, 'gpa.html', {'gpa': gpa, 'form':form})
    else:
        form = GPAForm()
    return render(request, 'gpa.html', {'form': form})



 
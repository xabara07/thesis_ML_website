"""thesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("personality", views.personality, name="personality"),
    path("predictions", views.predictions, name="predictions"),

    # admin
    path("analytics", views.analytics, name="analytics"),
    path("prediction", views.prediction, name="prediction"),
    path("students_list", views.students_list, name="students_list"),


    #personality type path
    path("personality/ESTJ", views.ESTJ, name= "ESTJ"),
    path("personality/ISTJ", views.ISTJ, name= "ISTJ"),
    path("personality/ENTJ", views.ENTJ, name= "ENTJ"),
    path("personality/INTJ", views.INTJ, name= "INTJ"),

    path("personality/ESTP", views.ESTP, name= "ESTP"),
    path("personality/ISTP", views.ISTP, name= "ISTP"),
    path("personality/ENTP", views.ENTP, name= "ENTP"),
    path("personality/INTP", views.INTP, name= "INTP"),

    path("personality/ESFJ", views.ESFJ, name= "ESFJ"),
    path("personality/ISFJ", views.ISFJ, name= "ISFJ"),
    path("personality/ENFJ", views.ENFJ, name= "ENFJ"),
    path("personality/INFJ", views.INFJ, name= "INFJ"),

    path("personality/ESFP", views.ESFP, name= "ESFP"),
    path("personality/ISFP", views.ISFP, name= "ISFP"),
    path("personality/ENFP", views.ENFP, name= "ENFP"),
    path("personality/INFP", views.INFP, name= "INFP"),

    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('takept/', views.take_pt, name="takept"),
    path('gpa/', views.calculate_gpa, name="gpa"),
    path("result/<str:pk>", views.result, name="result"),
    path("data/<str:pk>", views.data, name="data"),


    # Django Auth
    path('profile/', views.userprofile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('logout/', views.logoutUser, name="logout"),
    path("user/<str:pk_user>",views.user,name="user"),
    path("predict/", views.predict, name="predict"),
    path("update_data/<str:pk>",views.updateData,name="update_data"),
    path("delete_data/<str:pk>",views.deleteData,name="delete_data"),
    path("delete_stud/<str:pk>",views.deleteStud,name="delete_stud"),


    # Password Reset
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), 
    name="password_reset"),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
    name="password_reset_confirm"),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
    name="password_reset_complete"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

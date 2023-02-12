from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import student


def student_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='student')
        instance.groups.add(group)

        student.objects.create(
            user=instance,
            firstname = instance.username,
        )
        print('Profile created!')

post_save.connect(student_profile, sender=User)
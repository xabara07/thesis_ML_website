from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
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

@receiver(post_save, sender=User)
def add_user_to_admin_group(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        admin_group = Group.objects.get(name='admin')
        instance.groups.add(admin_group)

        # Remove the user from the "student" group, if they were accidentally added
        student_group = Group.objects.get(name='student')
        instance.groups.remove(student_group)

        # Delete the student profile, if it exists
        try:
            student_profile = student.objects.get(user=instance)
            student_profile.delete()
        except student.DoesNotExist:
            pass


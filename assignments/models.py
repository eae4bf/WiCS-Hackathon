from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    # computing_id = models.CharField(max_length=6, unique= True)
    bio = models.TextField()
    classes = models.ManyToManyField('Class',blank=True)
    assignments = models.ManyToManyField('Assignment',blank=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.user.username)




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()


class Class(models.Model):
    prefix = models.CharField(max_length=5)
    course_number = models.CharField(max_length=5)
    professor = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s Semester: %s" % (self.prefix, self.course_number, self.semester)



class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400, blank = True)
    course = models.CharField(max_length=400, blank=True, null=True)  # up to 1 optional relevant course
    due_date = models.DateTimeField(null=True) # captures time of object creation

    class Meta:
        ordering = ["-due_date"]
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SkillsSet(models.Model):
    skillname = models.CharField(max_length=250)

class AssessmentModel(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    skill = models.ManyToManyField(SkillsSet, related_name="userskilllist")

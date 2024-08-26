from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SkillsSet(models.Model):
    skillName = models.CharField(max_length=250)
    skillImage = models.ImageField()

class AssessmentModel(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    skill = models.ManyToManyField(SkillsSet, related_name="userskilllist")

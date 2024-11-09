from django.db import models

# Create your models here.
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    portfolio_website = models.URLField(blank=True, null=True)
    summary = models.TextField()


class Skill(models.Model):
    user = models.ForeignKey(UserProfile, related_name='skills', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)  # e.g., Programming Languages, Data Analytics
    skills = models.CharField(max_length=200)  # List of skills as a string


class Responsibility(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Experience(models.Model):
    user = models.ForeignKey(UserProfile, related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.ManyToManyField(Responsibility, blank=True)

    def __str__(self):
        return f"{self.position} at {self.company}"


class Education(models.Model):
    user = models.ForeignKey(UserProfile, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    completion_date = models.DateField()


class Certification(models.Model):
    user = models.ForeignKey(UserProfile, related_name='certifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)
    date = models.DateField()
    skills_covered = models.TextField()

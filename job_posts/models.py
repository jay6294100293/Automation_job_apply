from django.db import models

# Create your models here.
from django.db import models
from user_profiles.models import UserProfile

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    posted_time = models.CharField(max_length=50)
    published_at = models.DateField()
    job_url = models.URLField()
    company_name = models.CharField(max_length=100)
    company_url = models.URLField()
    description = models.TextField()
    applications_count = models.IntegerField()
    contract_type = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=50)
    work_type = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    poster_full_name = models.CharField(max_length=100)
    poster_profile_url = models.URLField()
    company_id = models.CharField(max_length=50)
    apply_url = models.URLField()
    apply_type = models.CharField(max_length=50)
    benefits = models.TextField(blank=True, null=True)

class Application(models.Model):
    user = models.ForeignKey(UserProfile, related_name='applications', on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applied_on = models.DateField(auto_now_add=True)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/')
    status = models.CharField(max_length=50)  # e.g., Pending, Rejected, Accepted

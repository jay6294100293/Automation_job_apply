# from django.db import models
# from user_profiles.models import UserProfile
#
# # Field choices for better data consistency
# CONTRACT_TYPE_CHOICES = [
#     ('Full-time', 'Full-time'),
#     ('Part-time', 'Part-time'),
#     ('Contract', 'Contract'),
#     ('Temporary', 'Temporary'),
#     ('Internship', 'Internship'),
# ]
#
# EXPERIENCE_LEVEL_CHOICES = [
#     ('Entry level', 'Entry level'),
#     ('Associate', 'Associate'),
#     ('Mid-Senior level', 'Mid-Senior level'),
#     ('Director', 'Director'),
#     ('Executive', 'Executive'),
# ]
#
# APPLICATION_STATUS_CHOICES = [
#     ('Pending', 'Pending'),
#     ('Accepted', 'Accepted'),
#     ('Rejected', 'Rejected'),
#     ('Interview', 'Interview'),
# ]
#
# CURRENCY_CHOICES = [
#     ('USD', 'USD'),
#     ('CAD', 'CAD'),
#     ('EUR', 'EUR'),
#     ('GBP', 'GBP'),
#     # Add more as needed
# ]
#
# class JobPosting(models.Model):
#     title = models.CharField(max_length=200)
#     location = models.CharField(max_length=100)
#     posted_time = models.CharField(max_length=50)
#     published_at = models.DateField()
#     job_url = models.URLField()
#     company_name = models.CharField(max_length=100)
#     company_url = models.URLField()
#     description = models.TextField()
#     applications_count = models.PositiveIntegerField()  # Changed to PositiveIntegerField for better data validation
#     contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE_CHOICES)
#     experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVEL_CHOICES)
#     work_type = models.CharField(max_length=100)
#     sector = models.CharField(max_length=100)
#     salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     salary_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='CAD')
#     poster_full_name = models.CharField(max_length=100)
#     poster_profile_url = models.URLField()
#     company_id = models.CharField(max_length=50)
#     apply_url = models.URLField()
#     apply_type = models.CharField(max_length=50)
#     benefits = models.TextField(blank=True, null=True)  # Optional field for additional job benefits
#
#     def __str__(self):
#         return f"{self.title} at {self.company_name}"
#
# class Application(models.Model):
#     user = models.ForeignKey(UserProfile, related_name='applications', on_delete=models.CASCADE)
#     job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
#     applied_on = models.DateField(auto_now_add=True)
#     resume = models.FileField(upload_to='resumes/')
#     cover_letter = models.FileField(upload_to='cover_letters/')
#     status = models.CharField(max_length=50, choices=APPLICATION_STATUS_CHOICES, default='Pending')
#
#     def __str__(self):
#         return f"Application by {self.user} for {self.job_posting.title}"
from django.core.exceptions import ValidationError
from django.db import models
from user_profiles.models import UserProfile

# Field choices for better data consistency
CONTRACT_TYPE_CHOICES = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Contract', 'Contract'),
    ('Temporary', 'Temporary'),
    ('Internship', 'Internship'),
]

EXPERIENCE_LEVEL_CHOICES = [
    ('Entry level', 'Entry level'),
    ('Associate', 'Associate'),
    ('Mid-Senior level', 'Mid-Senior level'),
    ('Director', 'Director'),
    ('Executive', 'Executive'),
]

APPLICATION_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
    ('Interview', 'Interview'),
]

CURRENCY_CHOICES = [
    ('USD', 'USD'),
    ('CAD', 'CAD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
    # Add more as needed
]


class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    posted_time = models.CharField(max_length=50)
    published_at = models.DateField()
    job_url = models.URLField()
    company_name = models.CharField(max_length=100)
    company_url = models.URLField()
    description = models.TextField()
    applications_count = models.PositiveIntegerField()
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE_CHOICES)
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVEL_CHOICES)
    work_type = models.CharField(max_length=100)  # Optional choices could be added
    sector = models.CharField(max_length=100)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='CAD')
    poster_full_name = models.CharField(max_length=100)
    poster_profile_url = models.URLField()
    company_id = models.CharField(max_length=50, unique=True)  # unique constraint added
    apply_url = models.URLField()
    apply_type = models.CharField(max_length=50)
    benefits = models.TextField(blank=True, null=True)

    def clean(self):
        if self.salary_min and self.salary_max and self.salary_min > self.salary_max:
            raise ValidationError("Minimum salary cannot be greater than maximum salary.")

    def __str__(self):
        return f"{self.title} at {self.company_name}"


class Application(models.Model):
    user = models.ForeignKey(UserProfile, related_name='applications', on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applied_on = models.DateField(auto_now_add=True)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/')
    status = models.CharField(max_length=50, choices=APPLICATION_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Application by {self.user} for {self.job_posting.title}"

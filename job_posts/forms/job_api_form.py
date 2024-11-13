from django import forms

PUBLISHED_AT_CHOICES = [
    ('anytime', 'Anytime'),
    ('past_month', 'Past Month'),
    ('past_week', 'Past Week'),
    ('past_24_hours', 'Past 24 Hours'),
]

JOB_TYPE_CHOICES = [
    ('full_time', 'Full-time'),
    ('part_time', 'Part-time'),
    ('contract', 'Contract'),
    ('temporary', 'Temporary'),
    ('internship', 'Internship'),
    ('volunteer', 'Volunteer'),
]

WORK_TYPE_CHOICES = [
    ('remote', 'Remote'),
    ('onsite', 'On-site'),
    ('hybrid', 'Hybrid'),
]

EXPERIENCE_LEVEL_CHOICES = [
    ('internship', 'Internship'),
    ('entry_level', 'Entry level'),
    ('associate', 'Associate'),
    ('mid_senior', 'Mid-Senior level'),
    ('director', 'Director'),
]

class JobSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=False, label="Job Title")
    location = forms.CharField(max_length=100, required=False, label="Location")
    published_at = forms.ChoiceField(choices=PUBLISHED_AT_CHOICES, required=False, label="Published At")
    rows = forms.IntegerField(min_value=1, max_value=100, initial=10, label="Total Results")
    work_type = forms.ChoiceField(choices=WORK_TYPE_CHOICES, required=False, label="Work Type")
    job_type = forms.MultipleChoiceField(choices=JOB_TYPE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple, label="Job Type")
    experience_level = forms.MultipleChoiceField(choices=EXPERIENCE_LEVEL_CHOICES, required=False, widget=forms.CheckboxSelectMultiple, label="Experience Level")

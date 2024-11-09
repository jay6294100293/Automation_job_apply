# from django.contrib import admin
# from .models import UserProfile, Skill, Experience, Education, Certification
#
# # Define inlines for related models
# class SkillInline(admin.TabularInline):
#     model = Skill
#     extra = 1  # Specifies how many extra forms to display
#     fields = ['category', 'skills']
#
# class ExperienceInline(admin.TabularInline):
#     model = Experience
#     extra = 1
#     fields = ['company', 'position', 'location', 'start_date', 'end_date', 'responsibilities']
#
# class EducationInline(admin.TabularInline):
#     model = Education
#     extra = 1
#     fields = ['degree', 'institution', 'location', 'completion_date']
#
# class CertificationInline(admin.TabularInline):
#     model = Certification
#     extra = 1
#     fields = ['title', 'organization', 'date', 'skills_covered']
#
# # Custom admin interface for UserProfile
# class UserProfileAdmin(admin.ModelAdmin):
#     inlines = [SkillInline, ExperienceInline, EducationInline, CertificationInline]
#     list_display = ('name', 'email', 'phone', 'location')  # Customize to display additional fields
#     search_fields = ('name', 'email', 'location', 'phone')  # Allow searching
#     list_filter = ('location',)  # Enable filtering by location
#
# # Register the admin class with the associated model
# admin.site.register(UserProfile, UserProfileAdmin)
# # No need to register Skill, Experience, Education, Certification if they're only accessed via inlines


from django.contrib import admin
from .models import UserProfile, Skill, Experience, Education, Certification, Responsibility

# Define inlines for related models
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1  # Specifies how many extra forms to display
    fields = ['category', 'skills']

class ResponsibilityInline(admin.TabularInline):
    model = Experience.responsibilities.through  # This allows adding responsibilities in the Experience inline
    extra = 1
    verbose_name = 'Responsibility'
    verbose_name_plural = 'Responsibilities'

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1
    fields = ['company', 'position', 'location', 'start_date', 'end_date']
    filter_horizontal = ['responsibilities']  # To make selecting responsibilities easier

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    fields = ['degree', 'institution', 'location', 'completion_date']

class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1
    fields = ['title', 'organization', 'date', 'skills_covered']

# Custom admin interface for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [SkillInline, ExperienceInline, EducationInline, CertificationInline]
    list_display = ('name', 'email', 'phone', 'location')  # Customize to display additional fields
    search_fields = ('name', 'email', 'location', 'phone')  # Allow searching
    list_filter = ('location',)  # Enable filtering by location

# Register the Responsibility model directly if you want to manage it separately
@admin.register(Responsibility)
class ResponsibilityAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)

# Register the admin class with the associated model
admin.site.register(UserProfile, UserProfileAdmin)
# No need to register Skill, Experience, Education, Certification if they're only accessed via inlines

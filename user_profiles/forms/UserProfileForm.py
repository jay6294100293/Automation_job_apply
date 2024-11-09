from django import forms

from user_profiles.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'location', 'phone', 'email', 'linkedin', 'portfolio_website', 'summary']

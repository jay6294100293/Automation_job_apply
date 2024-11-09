from django.forms import ModelForm

from user_profiles.models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'location', 'completion_date']

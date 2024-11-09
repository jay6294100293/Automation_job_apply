from django.forms import ModelForm, Textarea

from user_profiles.models import Experience


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'location', 'position', 'start_date', 'end_date', 'responsibilities']
        widgets = {
            'responsibilities': Textarea(attrs={'cols': 80, 'rows': 3}),
        }

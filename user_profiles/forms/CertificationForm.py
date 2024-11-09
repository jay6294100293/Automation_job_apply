from django.forms import ModelForm, Textarea

from user_profiles.models import Certification


class CertificationForm(ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'organization', 'date', 'skills_covered']
        widgets = {
            'skills_covered': Textarea(attrs={'cols': 80, 'rows': 2}),
        }

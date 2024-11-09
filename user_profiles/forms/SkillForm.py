from django.forms import ModelForm, Textarea

from user_profiles.models import Skill


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['category', 'skills']
        widgets = {
            'skills': Textarea(attrs={'cols': 40, 'rows': 1})
        }

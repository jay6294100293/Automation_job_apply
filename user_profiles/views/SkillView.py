# Add Skill View
from django.shortcuts import get_object_or_404, redirect, render

from user_profiles.forms.SkillForm import SkillForm
from user_profiles.models import Skill


def add_skill_view(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user.userprofile
            skill.save()
            return redirect('profile')
    else:
        form = SkillForm()
    return render(request, 'user_profiles/add_edit_skill.html', {'form': form})

# Edit Skill View
def edit_skill_view(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'user_profiles/add_edit_skill.html', {'form': form})

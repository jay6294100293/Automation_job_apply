# Add Experience View
from django.shortcuts import redirect, render, get_object_or_404

from user_profiles.forms.ExperienceForm import ExperienceForm
from user_profiles.models import Experience


def add_experience_view(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user.userprofile
            experience.save()
            return redirect('profile')
    else:
        form = ExperienceForm()
    return render(request, 'user_profiles/add_edit_experience.html', {'form': form})

# Edit Experience View
def edit_experience_view(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'user_profiles/add_edit_experience.html', {'form': form})

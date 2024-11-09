# Add Education View
from django.shortcuts import get_object_or_404, redirect, render

from user_profiles.forms.EducationForm import EducationForm
from user_profiles.models import Education


def add_education_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user.userprofile
            education.save()
            return redirect('profile')
    else:
        form = EducationForm()
    return render(request, 'user_profiles/add_edit_education.html', {'form': form})




def edit_education_view(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EducationForm(instance=education)
    return render(request, 'user_profiles/add_edit_education.html', {'form': form})

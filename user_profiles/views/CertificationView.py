# Add Certification View
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from user_profiles.forms.CertificationForm import CertificationForm


def add_certification_view(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.user = request.user.userprofile
            certification.save()
            return redirect('profile')
    else:
        form = CertificationForm()
    return render(request, 'user_profiles/add_edit_certification.html', {'form': form})

# Edit Certification View
def edit_certification_view(request, pk):
    certification = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CertificationForm(instance=certification)
    return render(request, 'user_profiles/add_edit_certification.html', {'form': form})

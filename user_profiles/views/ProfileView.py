from django.shortcuts import render, redirect

from user_profiles.forms.UserProfileForm import UserProfileForm
from user_profiles.models import UserProfile


def profile_view(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
        'skills': user_profile.skills.all(),
        'experiences': user_profile.experiences.all(),
        'education': user_profile.education.all(),
        'certifications': user_profile.certifications.all(),
    }
    return render(request, 'user_profiles/profile.html', context)


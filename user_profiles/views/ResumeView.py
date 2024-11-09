from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from weasyprint import HTML

from user_profiles.models import UserProfile


def resume_view(request, user_id):
    profile = get_object_or_404(UserProfile, id=user_id)
    # Assuming UserProfile model has related names set up for skills, experiences, etc.
    context = {
        'profile': profile,
        'skills': profile.skills.all(),
        'experiences': profile.experiences.prefetch_related('responsibilities').all(),
        'educations': profile.education.all(),
        'certifications': profile.certifications.all(),
    }
    return render(request, 'user_profiles/resume.html', context)

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.shortcuts import get_object_or_404
from user_profiles.models import UserProfile

def generate_pdf_view(request, user_id):
    profile = get_object_or_404(UserProfile, id=user_id)
    context = {
        'profile': profile,
        'skills': profile.skills.all(),
        'experiences': profile.experiences.prefetch_related('responsibilities').all(),
        'educations': profile.education.all(),
        'certifications': profile.certifications.all(),
    }

    # Render the HTML template to a string
    html_string = render_to_string('user_profiles/resume_template.html', context)

    # Generate a PDF using WeasyPrint
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{profile.name}_resume.pdf"'

    HTML(string=html_string).write_pdf(response)

    return response

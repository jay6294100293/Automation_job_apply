from django.urls import path

from user_profiles.views.ResumeView import resume_view, generate_pdf_view

urlpatterns = [
    path('resume/<int:user_id>/', resume_view, name='resume'),

    path('resume/<int:user_id>/download-pdf/', generate_pdf_view, name='download_resume_pdf'),

]

from django.urls import path

from job_posts.views.job_api_views import fetch_and_store_job_postings

urlpatterns = [
    path('fetch-job-postings/', fetch_and_store_job_postings, name='fetch_job_postings'),
]

from django.shortcuts import render
from django.http import JsonResponse
from apify_client import ApifyClient
from datetime import datetime, timedelta

import os

from job_posts.forms.job_api_form import JobSearchForm
from job_posts.models import JobPosting

client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

def fetch_and_store_job_postings(request):
    if request.method == 'POST':
        form = JobSearchForm(request.POST)
        if form.is_valid():
            # Extract form data
            title = form.cleaned_data['title']
            location = form.cleaned_data['location']
            published_at = form.cleaned_data['published_at']
            rows = form.cleaned_data['rows']
            work_type = form.cleaned_data['work_type']
            job_type = form.cleaned_data['job_type']
            experience_level = form.cleaned_data['experience_level']

            # Map 'published_at' choice to a date range filter
            if published_at == 'past_month':
                published_at = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            elif published_at == 'past_week':
                published_at = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
            elif published_at == 'past_24_hours':
                published_at = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
            else:
                published_at = ""

            # Prepare API request data
            run_input = {
                "title": title,
                "location": location,
                "publishedAt": published_at,
                "rows": rows,
                "workType": work_type,
                "jobType": job_type,
                "experienceLevel": experience_level,
                "proxy": {
                    "useApifyProxy": True,
                    "apifyProxyGroups": ["RESIDENTIAL"],
                },
            }

            # Run the API request
            run = client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
            for item in client.dataset(run["defaultDatasetId"]).iterate_items():
                JobPosting.objects.update_or_create(
                    job_url=item['jobUrl'],
                    defaults={
                        'title': item['title'],
                        'location': item['location'],
                        'posted_time': item['postedTime'],
                        'published_at': datetime.strptime(item['publishedAt'], "%Y-%m-%d").date() if 'publishedAt' in item else None,
                        'company_name': item['companyName'],
                        'company_url': item['companyUrl'],
                        'description': item['description'],
                        'applications_count': int(item['applicationsCount'].split()[0]) if 'applicationsCount' in item else 0,
                        'contract_type': item.get('contractType', 'Full-time'),
                        'experience_level': item.get('experienceLevel', 'Entry level'),
                        'work_type': item.get('workType', ''),
                        'sector': item.get('sector', ''),
                        'salary_min': float(item['salary'].split('-')[0].replace('CA$', '').replace(',', '').strip()) if '-' in item['salary'] else None,
                        'salary_max': float(item['salary'].split('-')[1].replace('CA$', '').replace(',', '').strip()) if '-' in item['salary'] else None,
                        'salary_currency': 'CAD',
                        'poster_full_name': item['posterFullName'],
                        'poster_profile_url': item['posterProfileUrl'],
                        'company_id': item['companyId'],
                        'apply_url': item['applyUrl'],
                        'apply_type': item['applyType'],
                        'benefits': item.get('benefits', ''),
                    }
                )
            return JsonResponse({'status': 'success', 'message': 'Job postings have been successfully fetched and stored.'})
    else:
        form = JobSearchForm()

    return render(request, 'job_search_form.html', {'form': form})

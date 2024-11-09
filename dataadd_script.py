from datetime import date
from django.db import transaction
from user_profiles.models import UserProfile, Skill, Experience, Education, Certification, Responsibility  # Replace 'your_app' with the actual app name



# Create UserProfile instance
user_profile = UserProfile.objects.create(
    name="Mrityunjay Gupta",
    location="Burnaby, BC",
    phone="778-636-6294",
    email="mrityunjay.100293@gmail.com",
    linkedin="https://linkedin.com/in/gupta-mrityunjay",
    portfolio_website="https://portfolio-website.com",
    summary=(
        "Data-driven professional with over 5 years of experience in software development, data analysis, "
        "and machine learning, recently graduated with a Master's in Analytics. Skilled in extracting insights "
        "from complex datasets, developing predictive models, and creating analytical dashboards to support "
        "data-informed decisions. Recognized for strong problem-solving abilities, proficiency in data modeling, "
        "and expertise in machine learning and statistical analysis. Awarded first place at the Data Analytics "
        "Association Hackathon for innovative wildfire prevention solutions."
    )
)

# Use a transaction to ensure all operations are atomic
with transaction.atomic():
    # Adding skills
    skills = [
        ("Programming Languages", "Python, SQL, R, JavaScript"),
        ("Data Analytics", "Data Wrangling, Data Cleaning, Data Visualization (Tableau, Matplotlib, Seaborn), Machine Learning (Scikit-Learn, TensorFlow)"),
        ("Software Development", "Full-Stack Development (Django, Flask), RESTful APIs, Version Control (Git/GitHub), CI/CD (Docker, Jenkins)"),
        ("Database Management", "MySQL, PostgreSQL, MongoDB, Amazon Redshift"),
        ("Big Data & Cloud Platforms", "AWS (S3, EC2, Lambda), GCP, Spark"),
    ]

    for category, skills_list in skills:
        Skill.objects.create(user=user_profile, category=category, skills=skills_list)

    # Adding experiences and handling responsibilities
    experiences = [
        {
            "company": "Focus College",
            "location": "Surrey, BC",
            "position": "Software Developer / Analyst Professor",
            "start_date": date(2023, 9, 1),
            "end_date": date(2024, 4, 1),
            "responsibilities": [
                "Led advanced courses on software development and data analysis, covering Python, machine learning, and data visualization, mentoring over 100 students.",
                "Designed hands-on projects focused on real-world applications of data analytics, enabling students to gain practical industry-ready skills.",
                "Conducted workshops on data storytelling and visualization techniques to help students effectively communicate insights."
            ]
        },
        {
            "company": "Era Interfaces Pvt Ltd",
            "location": "Bengaluru, India",
            "position": "Backend Developer / Machine Learning Engineer",
            "start_date": date(2020, 6, 1),
            "end_date": date(2022, 5, 1),
            "responsibilities": [
                "Engineered and optimized backend solutions for data-intensive applications, enhancing data pipeline efficiency by 30%.",
                "Developed and deployed machine learning models that improved data processing speed by 25% and significantly increased prediction accuracy.",
                "Collaborated closely with cross-functional teams to identify data gaps and implement improvements, reducing data discrepancies by 20%."
            ]
        },
        {
            "company": "Indian Institute Of Hardware Technology",
            "location": "Bengaluru, India",
            "position": "Software Trainer",
            "start_date": date(2020, 1, 1),
            "end_date": date(2020, 8, 1),
            "responsibilities": [
                "Trained and guided students in programming, data analysis, and visualization using Python, SQL, and key analytics tools.",
                "Introduced interactive, project-based learning modules that boosted engagement and reinforced core data analysis skills.",
                "Conducted assessment workshops, providing personalized feedback to over 50 students to ensure strong foundational understanding."
            ]
        },
        {
            "company": "Lov.Cash India Pvt Ltd",
            "location": "Bengaluru, India",
            "position": "Software Developer",
            "start_date": date(2019, 4, 1),
            "end_date": date(2020, 1, 1),
            "responsibilities": [
                "Developed and maintained dynamic web applications, integrating real-time data analysis features to enhance user experience.",
                "Worked alongside data teams to design optimized ETL processes, cutting down data processing time by 15%.",
                "Led the implementation of quality control measures in software projects, reducing error rates in deployments by 10%."
            ]
        },
        {
            "company": "W3Turbo India Pvt Ltd",
            "location": "Banaras, India",
            "position": "Software Developer",
            "start_date": date(2016, 10, 1),
            "end_date": date(2019, 1, 1),
            "responsibilities": [
                "Designed, implemented, and tested software solutions for diverse client projects, ensuring data integrity and optimal system performance.",
                "Improved backend systems through modular designs and efficient algorithms, reducing server load by 20%."
            ]
        }
    ]

    for exp in experiences:
        experience = Experience(
            user=user_profile,
            company=exp["company"],
            location=exp["location"],
            position=exp["position"],
            start_date=exp["start_date"],
            end_date=exp["end_date"]
        )
        experience.save()
        for resp_desc in exp["responsibilities"]:
            resp, created = Responsibility.objects.get_or_create(description=resp_desc)
            experience.responsibilities.add(resp)

    # Adding education details
    education_details = [
        {
            "degree": "Master's of Professional Studies in Analytics",
            "institution": "Northeastern University",
            "location": "Vancouver, BC",
            "completion_date": date(2024, 5, 1)
        },
        {
            "degree": "Bachelor of Technology in Computer Science",
            "institution": "Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology",
            "location": "Chennai, India",
            "completion_date": date(2016, 8, 1)
        }
    ]

    for edu in education_details:
        Education.objects.create(user=user_profile, **edu)

    # Adding certifications
    certifications = [
        {
            "title": "TensorFlow for Convolutional Neural Networks (CNNs)",
            "organization": "Coursera",
            "date": date(2023, 9, 1),
            "skills_covered": "Deep Learning, CNNs, TensorFlow, Image Recognition"
        },
        {
            "title": "Introduction to TensorFlow for AI, Machine Learning, and Deep Learning",
            "organization": "Coursera",
            "date": date(2023, 8, 1),
            "skills_covered": "Machine Learning, Neural Networks, TensorFlow, Model Deployment"
        },
        {
            "title": "Python for Data Science, AI & Development",
            "organization": "Coursera",
            "date": date(2023, 8, 1),
            "skills_covered": "Python Programming, Data Wrangling, Machine Learning Basics, Data Analysis"
        },
        {
            "title": "Data Visualization and Storytelling Basics",
            "organization": "Northeastern University",
            "date": date(2023, 1, 1),
            "skills_covered": "Data Visualization, Storytelling, Tableau, Data Communication"
        },
        {
            "title": "Introduction to Analytics",
            "organization": "Northeastern University",
            "date": date(2022, 12, 2),
            "skills_covered": "Analysis of Data, Analytics, Central Tendency, Data Visualization, Probability, Strategic Decision Making, Variance"
        }
    ]

    for cert in certifications:
        Certification.objects.create(user=user_profile, **cert)

print("Resume data added successfully!")

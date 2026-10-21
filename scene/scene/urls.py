from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from courses import views

from .settings import ADMIN_ENABLED

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('', views.main, name="main"),
    path('progress/', views.progress, name="progress"),
    path('courses/', include('courses.urls')),
    path('signup/', views.signup, name = 'signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), 
    path('login/', views.login, name = 'login'),
    path("accounts/", include("allauth.urls")),
    path('captcha/', include('captcha.urls')),
    path('user/', views.user, name="user"),
    path('delete_account/', views.delete_account, name="delete_account"),
    path('run_task/', views.run_task, name = 'run_task'),
    path('save_task/', views.save_task, name = 'save_task'),
    path('finish_course/', views.finish_course, name = 'finish_course'),
    path('finish_chapter/', views.finish_chapter, name = 'finish_chapter'),

    path("terms_of_use/", views.terms_of_use, name = 'terms_of_use'),
    path("privacy/", views.privacy, name = 'privacy'),
    path("terms/", views.terms, name = 'terms'),
    path("donation/", views.donation, name = 'donation'),
    path("", include("django_prometheus.urls")),
    path('csrf_failure', views.csrf_failure, name = 'csrf_failure'),
    path("authors/<str:author>/", views.author, name="author"),
    path("authors/", views.authors, name="authors"),

    path('playground/<str:lang_id>/', views.playground, name="playground"),
    path('playground/', views.playgrounds, name="playgrounds"),
    path('create_playground/', views.create_playground, name="create_playground"),
    path('run_code/', views.run_code, name="run_code"),

    path('handle_practice_code/', views.handle_practice_code, name="handle_practice_code"),
    path('download_project/', views.download_project, name="download_project"),
    path('download_project_archive/', views.download_project_archive, name="download_project_archive"),
]

if ADMIN_ENABLED:
    urlpatterns.append(path('admin/', admin.site.urls))

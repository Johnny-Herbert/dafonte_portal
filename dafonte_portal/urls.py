"""dafonte_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from portal.views import (
    HomeView, PracticeAreaListView, PracticeAreaDetailView, WhoWeAreView,
    CultureView, AwardListView, PressListView, ArticleListView,
    ArticleDetailView, EventListView, EventDetailView,
    SocialResponsabilityView, ContactView, PressDetailView,
    SpecializationSectorDetailView, InstitutionalFolderView, 
    CodeConductView, PrivacyPolicy, ComplianceView, CollaborationView,
    InformativeListView, InformativeDetailView
)
from applying.views import OpportunityView, ApplyToPdf


urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("", HomeView.as_view(), name="home"),
    path("occupation-areas/", PracticeAreaListView.as_view(),
         name="practice-area-list"),
    path("practice-areas/<int:practice_id>/",
         PracticeAreaDetailView.as_view(), name="practice-area-detail"),
    path("specialization-sectors/<int:sector_id>/",
         SpecializationSectorDetailView.as_view(),
         name="specialization-sector-detail"),
    path("members/", include("members.urls")),
    path("who-we-are/", WhoWeAreView.as_view(), name="who-we-are"),
    path("culture/", CultureView.as_view(), name="culture"),
    path("awards/", AwardListView.as_view(), name="award-list"),
    path("publications/press/", PressListView.as_view(), name="press-list"),
    path("publications/press/<int:press_pk>/",
         PressDetailView.as_view(), name="press-detail"),
    path("publications/article/",
         ArticleListView.as_view(), name="article-list"),
    path("publications/article/<int:article_pk>/",
         ArticleDetailView.as_view(), name="article-detail"),
    path("publications/informative/",
         InformativeListView.as_view(), name="informative-list"),
    path("publications/informative/<int:informative_pk>/",
         InformativeDetailView.as_view(), name="informative-detail"),
    path("events/", EventListView.as_view(), name="event-list"),
    path("events/<int:event_pk>/",
         EventDetailView.as_view(), name="event-detail"),
    path("social-responsability/",
         SocialResponsabilityView.as_view(), name="social-responsability"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("opportunity/<int:opportunity_id>/",
         OpportunityView.as_view(), name="opportunity-detail"),
    path("opportunity/", OpportunityView.as_view(), name="opportunity"),
    path("pdf/dafonte-folder-institucional.pdf",
         InstitutionalFolderView.as_view(), name="institutional-folder"),
    path("apply/<int:apply_id>/", ApplyToPdf.as_view(), name="apply-pdf"),
    path("api/", include("api.urls")),
    path("compliance/", ComplianceView.as_view(), name="compliance"),
    path("collaboration/", CollaborationView.as_view(), name="collaboration"),
    path("pdf/codigo-de-conduta-e-etica.pdf",
         CodeConductView.as_view(), name="code-of-conduct"),
     path("pdf/privacy-policy.pdf",
         PrivacyPolicy.as_view(), name="privacy-policy"),

    # url(r"^files/(?P<file_name>[\w\-\./]*)$", UploadedFilesView.as_view(),
    #     name="upfiles")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

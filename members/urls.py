from django.urls import path
from members.views import MemberListView, MemberDetailView


urlpatterns = [
    path("", MemberListView.as_view(), name="member-list"),
    path("<int:member_id>/", MemberDetailView.as_view(), name="member-detail"),
]

from django.urls import path
from .views import CandidatesAPIView

urlpatterns = [
    path(
        "create",
        CandidatesAPIView.as_view(),
        name="candidate-list",
    ),
    path(
        "<int:candidate_id>",
        CandidatesAPIView.as_view(),
        name="candidate-detail",
    ),
    path(
        "search/",
        CandidatesAPIView.as_view(),
        name="candidate-search",
    ),
]

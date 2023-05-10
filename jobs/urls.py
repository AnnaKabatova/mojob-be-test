from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import GetUserApplicationsView, JobWithHeaderViewSet

router = SimpleRouter()
router.register("jobs", JobWithHeaderViewSet, basename="jobs")

app_name = "jobs"

urlpatterns = [
    path("", include(router.urls)),
    path(
        "users/<int:user_id>/applications/",
        GetUserApplicationsView.as_view(),
        name="get_user_applications",
    ),
]

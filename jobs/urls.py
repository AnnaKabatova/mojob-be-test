from django.urls import path
from .views import (
    CreateJobWithHeaderView,
    UpdateJobWithHeaderView,
    DeleteJobWithHeaderView,
    GetJobWithSerializedHeaderView,
    GetUserApplicationsView
)


app_name = "jobs"

urlpatterns = [
    path('jobs/', CreateJobWithHeaderView.as_view(), name='create_job'),
    path('jobs/<int:pk>/', UpdateJobWithHeaderView.as_view(), name='update_job'),
    path('jobs/<int:pk>/delete/', DeleteJobWithHeaderView.as_view(), name='delete_job'),
    path('jobs/<int:pk>/header/', GetJobWithSerializedHeaderView.as_view(), name='get_job_header'),
    path('users/<int:user_id>/applications/', GetUserApplicationsView.as_view(), name='get_user_applications'),
]

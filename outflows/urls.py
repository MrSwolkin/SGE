from django.urls import path
from . import views


urlpatterns = [
    path("outflows/list", views.OutflowListView.as_view(), name="outflow_list"),
    path("outflows/create", views.OutflowCreateView.as_view(), name="outflow_create"),
    path("outflows/<int:pk>/details", views.OutflowDetailsView.as_view(), name="outflow_details"),

    path("api/v1/outflows/", views.OutflowCreateListAPIView.as_view(), name="outflow-create-list-api-view"),
    path("api/v1/outflows/<int:pk>", views.OutflowRetrieveAPIView.as_view(), name="outflow-details-api-view")
]

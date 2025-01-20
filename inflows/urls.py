from django.urls import path
from . import views


urlpatterns = [
    path("inflows/list/", views.InflowListView.as_view(), name="inflow_list"),
    path("inflows/create/", views.InflowCreateView.as_view(), name="inflow_create"),
    path("inflows/<int:pk>/details/", views.InflowDetailsView.as_view(), name="inflow_details"),

    path("api/v1/inflows/", views.InflowCreateListAPIView.as_view(), name="inflow-create-list-api-view"),
    path("api/v1/inflows/<int:pk>/", views.InflowRetrieveAPIView.as_view(), name="inflow-details-api-view"),
]

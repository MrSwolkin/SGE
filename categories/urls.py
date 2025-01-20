from django.urls import path
from . import views


urlpatterns = [
    path("categories/list/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/create/", views.CategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/details/", views.CategoryDetailsView.as_view(), name="category_details"),
    path("categories/<int:pk>/update/", views.CategoryUpdateView.as_view(), name="category_update"),
    path("categories/<int:pk>/delete/", views.CategoryDeleteView.as_view(), name="category_delete"),

    path("api/v1/categories/", views.CategoryCreateListAPIView.as_view(), name="categories-create-list-api-view"),
    path("api/v1/categories/<int:pk>/", views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name="categories-details-api-view"),
]

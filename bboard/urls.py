from django.urls import path
from .views import (
    NewsCreateView,
    NewsListView,
    NewsDetailView,
    NewsVoiceUpdateView,
    CommentCreateView,
    CommentListView,
    CommentDetailView,
    BbCreateView,
    BbEditView,
    BbDeleteView,
    BbByRubricView,
    BbDetailView,
    index,
)

api_base = "api/v1/news/"

urlpatterns = [
    # API NEWS
    path(api_base + "create/", NewsCreateView.as_view()),
    path(api_base + "all/", NewsListView.as_view()),
    path(api_base + "detail/<int:pk>/", NewsDetailView.as_view()),
    path(api_base + "voice/", NewsVoiceUpdateView.as_view()),
    # API COMMENTS
    path(api_base + "comments/create/<int:pk>/", CommentCreateView.as_view()),
    path(api_base + "comments/all/", CommentListView.as_view()),
    path(api_base + "comments/detail/<int:pk>/", CommentDetailView.as_view()),
    # SITE URLS
    path("add/", BbCreateView.as_view(), name="add"),
    path("edit/<int:pk>/", BbEditView.as_view(), name="edit"),
    path("delete/<int:pk>", BbDeleteView.as_view(), name="delete"),
    path("<int:rubric_id>/", BbByRubricView.as_view(), name="by_rubric"),
    path("detail/<int:pk>/", BbDetailView.as_view(), name="detail"),
    path("", index, name="index"),
]

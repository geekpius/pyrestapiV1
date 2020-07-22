from django.urls import path
from news.api.views import article_list_create_api_view


app_name = "news"

urlpatterns = [
    path("articles/", article_list_create_api_view, name="article-list")
]
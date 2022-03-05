from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
  path('', views.PostList.as_view(), name="home"),
  path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
  path('author/<slug:slug>/', views.AuthorView.as_view(), name="author"),
  path('post/search/results', views.SearchResultsView.as_view(), name='search_results'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

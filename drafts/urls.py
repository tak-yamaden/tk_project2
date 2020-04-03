from django.urls import path

from .views import DraftListView, DraftDetailView, SearchResultListView, CategoryListView, SearchResult2ListView

urlpatterns = [
    path('', DraftListView.as_view(), name='draft_list'),
    path('<uuid:pk>', DraftDetailView.as_view(), name='draft_detail'),
    path('search_results/', SearchResultListView.as_view(), name='search_results'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('search_results2/',SearchResult2ListView.as_view(), name='search_results2'),
]
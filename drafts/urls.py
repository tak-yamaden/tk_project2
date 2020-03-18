from django.urls import path

from .views import DraftListView, DraftDetailView, SearchResultListView

urlpatterns = [
    path('', DraftListView.as_view(), name='draft_list'),
    path('<uuid:pk>', DraftDetailView.as_view(), name='draft_detail'),
    path('search_results/', SearchResultListView.as_view(), name='search_results'),

]
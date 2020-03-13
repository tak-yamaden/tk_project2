from django.urls import path

from .views import DraftListView, DraftDetailView

urlpatterns = [
    path('', DraftListView.as_view(), name='draft_list'),
    path('<uuid:pk>', DraftDetailView.as_view(), name='draft_detail'),
]
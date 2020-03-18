from django.urls import path

from .views import HomePageView, AboutPAgeView, SearchPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPAgeView.as_view(), name='about'),
    path('search/', SearchPageView.as_view(), name='search'),
]
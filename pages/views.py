from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPAgeView(TemplateView):
    template_name = 'about.html'

class SearchPageView(TemplateView):
    template_name = 'search.html'


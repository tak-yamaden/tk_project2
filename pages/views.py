from django.views.generic import TemplateView
from drafts.models import Category, Draft

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category_list'] = Category.objects.all()
        return ctx

class AboutPAgeView(TemplateView):
    template_name = 'about.html'


class SearchPageView(TemplateView):
    template_name = 'search.html'


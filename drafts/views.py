from django.views.generic import ListView, DetailView

from .models import Draft

class DraftListView(ListView):
    model = Draft
    context_object_name = 'draft_list'
    template_name = 'drafts/draft_list.html'

class DraftDetailView(DetailView):
    model = Draft
    template_name = 'drafts/draft_detail.html'
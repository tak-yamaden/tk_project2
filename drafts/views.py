from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Draft

class DraftListView(LoginRequiredMixin, ListView):
    model = Draft
    context_object_name = 'draft_list'
    template_name = 'drafts/draft_list.html'
    login_url = 'account_login'

class DraftDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Draft
    context_object_name = 'draft'
    template_name = 'drafts/draft_detail.html'
    login_url = 'account_login'
    permission_required = 'drafts.special_status'
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Draft, Category, Person


class DraftListView(LoginRequiredMixin, ListView):
    model = Draft
    context_object_name = 'draft_list'
    template_name = 'drafts/draft_list.html'
    login_url = 'account_login'
    paginate_by = 5


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'drafts/category_list.html'
    login_url = 'account_login'
    paginate_by = 4


class DraftDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Draft
    context_object_name = 'draft'
    template_name = 'drafts/draft_detail.html'
    login_url = 'account_login'
    permission_required = 'drafts.special_status'


class SearchResultListView(LoginRequiredMixin, ListView):
    model = Draft
    context_object_name = 'draft_list'
    template_name = 'drafts/search_results.html'
    login_url = 'account_login'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        return Draft.objects.filter(
            Q(product_name__icontains=query) | Q(company_name__icontains=query) | Q(category__address=query))\
            .filter(is_active=True)


class SearchResult2ListView(LoginRequiredMixin, ListView):
    model = Draft
    context_object_name = 'draft_list'
    template_name = 'drafts/search_results2.html'
    login_url = 'account_login'
    paginate_by = 2

    def get_queryset(self):
        return Draft.objects.filter(is_active=False)


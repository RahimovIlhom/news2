from django.db.models import Q
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from hitcount.models import HitCount
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

from .models import New, Category, Comment
from .forms import ContactMessageForm, CommentCreateForm, ReplyCommentCreateForm


# Create your views here.


def home_page_view(request):
    all_news = New.published.all().order_by('-publish_time')
    last_three_news = all_news[:3]
    football_news = all_news[3:7]
    all_categories = Category.objects.all()

    # featured news
    featured_news = [[news, news.comments.count()] for news in all_news]
    featured_news = sorted(featured_news, key=lambda news: news[1])
    featured_news = [news[0] for news in reversed(featured_news)]

    # trending news
    trending_news = [[news, HitCount.objects.get_for_object(news).hits] for news in all_news]
    trending_news = sorted(trending_news, key=lambda news: news[1])
    trending_news = [news[0] for news in reversed(trending_news)]

    context = {
        'three_news': last_three_news,
        'football_news': football_news,
        'categories': all_categories,
        'featured_news': featured_news[:10],
        'trending_news': trending_news[:20],
        'last_news': all_news[:20],
    }

    return render(request, 'news/index.html', context=context)


def category_page_view(request):
    return render(request, 'news/category.html')


def single_page_view(request):
    return render(request, 'news/single.html')


def contact_page_view(request):
    form = ContactMessageForm(request.POST or None)
    context = {
        'form': form
    }
    if request.POST and form.is_valid():
        form.save()
        return render(request, 'news/contact.html', context)
    return render(request, 'news/contact.html', context)


def news_detail_view(request, slug):
    new = New.published.get(slug=slug)
    comments = Comment.objects.filter(news=new)
    hitcontext = {}
    # hit count logic
    hitcount = get_hitcount_model().objects.get_for_object(new)
    hits = hitcount.hits
    hitcontext['hitcount'] = {'pk': hitcount.pk}
    hit_count_response = HitCountMixin.hit_count(request, hitcount)
    if hit_count_response.hit_counted:
        hits += 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits
    new_comment = None
    new_reply_comment = None
    if request.method == 'POST':
        comment_form = CommentCreateForm(data=request.POST)
        reply_comment_form = ReplyCommentCreateForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = new
            new_comment.user = request.user
            new_comment.save()
        elif reply_comment_form.is_valid():
            new_reply_comment = reply_comment_form.save(commit=False)
            new_reply_comment.comment = comments[0]
            new_reply_comment.user = request.user
            new_reply_comment.save()
    else:
        comment_form = CommentCreateForm()
        reply_comment_form = ReplyCommentCreateForm()
    context = {
        'news': new,
        'comments': comments,
        'comment_form': comment_form,
        'reply_comment_form': reply_comment_form,
        'new_comment': new_comment,
        'new_reply_comment': new_reply_comment
    }

    return render(request, 'news/single.html', context)


class SearchResultView(ListView):
    model = New
    template_name = 'news/search.html'
    context_object_name = 'search_news'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return New.published.filter(
            Q(title__icontains=query) | Q(body__icontains=query) | Q(summary__icontains=query)
        ).order_by('-publish_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        query_set = self.get_queryset()
        context['search_news'] = query_set[:2]
        context['search_news_all'] = query_set[2:]
        return context


class CategoryNewsListView(DetailView):
    model = Category
    template_name = 'news/category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['category_news_short'] = New.published.filter(category=category)[:2]
        context['category_news'] = New.published.filter(category=category)[2:]
        return context




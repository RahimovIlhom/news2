from django.urls import path
from .views import (
    home_page_view,
    contact_page_view,
    category_page_view,
    news_detail_view,
    SearchResultView,
    CategoryNewsListView,
)


urlpatterns = [
    path('', home_page_view, name='home'),
    path('categories/', category_page_view, name='categories'),
    path('news/<slug>/', news_detail_view, name='single'),
    path('contact/', contact_page_view, name='contact'),
    path('search/', SearchResultView.as_view(), name='search'),
    path('category/<slug>/', CategoryNewsListView.as_view(), name='category_news'),
]

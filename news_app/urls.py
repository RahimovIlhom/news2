from django.urls import path
from .views import home_page_view, contact_page_view, category_page_view, single_page_view


urlpatterns = [
    path('', home_page_view, name='home'),
    path('categories/', category_page_view, name='categories'),
    path('single/', single_page_view, name='single'),
    path('contact/', contact_page_view, name='contact'),
]

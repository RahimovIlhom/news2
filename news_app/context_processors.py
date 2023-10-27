# context_processors.py
from news_app.models import Category, New


def categories(request):
    all_categories = Category.objects.all()

    return {'categories': all_categories}

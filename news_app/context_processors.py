# context_processors.py
from hitcount.models import HitCount

from news_app.models import Category, New


def categories(request):
    all_categories = Category.objects.all()

    return {'categories': all_categories}


def trending_news(request):
    all_news = New.published.all().order_by('-publish_time')

    # trending news
    trend_news = [[news, HitCount.objects.get_for_object(news).hits] for news in all_news]
    trend_news = sorted(trend_news, key=lambda news: news[1])
    trend_news = [news[0] for news in reversed(trend_news)]

    # popular news
    popular_news = [[news, news.comments.count()] for news in trend_news[:100]]
    popular_news = sorted(popular_news, key=lambda obj: obj[1])
    popular_news = [news[0] for news in reversed(popular_news)]

    return {
        'trending_news': trend_news[:20],
        'popular_news': popular_news[:3],
    }


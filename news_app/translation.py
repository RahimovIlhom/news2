from modeltranslation.translator import register, TranslationOptions, translator
from .models import New, Category


@register(New)
class NewsTranslationOptions(TranslationOptions):
    fields = ['title', 'summary', 'body']


# translator.register(New, NewsTranslationOptions)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ['name']

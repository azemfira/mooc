from django.contrib import admin
from .models import Article, ArticleSeries

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        'author',
        # 'published'
    ]

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['title', 'subtitle', 'article_slug', 'series', 'author']}),
        ("Content", {"fields": ['content','content1','content2', 'notes']}),
        ("Date", {"fields": ['modified']})
    ]

# Register your models here.
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArticleAdmin)

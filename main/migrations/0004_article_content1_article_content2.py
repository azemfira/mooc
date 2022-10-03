# Generated by Django 4.1.1 on 2022-10-02 16:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_article_author_articleseries_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content1',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='content2',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
    ]

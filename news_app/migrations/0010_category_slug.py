# Generated by Django 4.2.7 on 2023-11-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0009_category_name_en_category_name_ru_category_name_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=models.CharField(max_length=255), max_length=255),
        ),
    ]

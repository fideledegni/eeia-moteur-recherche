# Generated by Django 3.2.4 on 2021-07-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_text', models.CharField(max_length=200)),
                ('search_date', models.DateTimeField(verbose_name='search date')),
                ('clicked_article_1', models.CharField(max_length=200)),
                ('clicked_article_2', models.CharField(max_length=200)),
                ('clicked_article_3', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 4.0 on 2022-02-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_alter_blog_options_blog_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=80, unique=True),
        ),
    ]
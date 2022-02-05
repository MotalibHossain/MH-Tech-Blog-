# Generated by Django 4.0 on 2022-02-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AddField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(verbose_name='What is on your mind?'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='Articles/', verbose_name='Image'),
        ),
    ]

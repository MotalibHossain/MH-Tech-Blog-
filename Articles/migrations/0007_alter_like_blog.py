# Generated by Django 4.0 on 2022-02-05 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0006_alter_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_like', to='Articles.blog'),
        ),
    ]

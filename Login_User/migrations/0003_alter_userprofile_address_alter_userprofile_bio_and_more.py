# Generated by Django 4.0 on 2021-12-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_User', '0002_alter_userprofile_address_alter_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

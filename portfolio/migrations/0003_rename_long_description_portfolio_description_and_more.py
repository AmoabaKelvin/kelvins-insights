# Generated by Django 4.0.3 on 2022-09-10 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_reddit_portfolio_twitter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='long_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='education',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='skills',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-14 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_newsletter_newslettersubscribers_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='BlogLike',
        ),
    ]

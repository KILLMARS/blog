# Generated by Django 5.1.6 on 2025-02-23 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]

# Generated by Django 4.2 on 2023-05-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_topic_highlighted_topic_language_topic_linenos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='code',
            field=models.TextField(blank=True, null=True, verbose_name='Dastur kodi'),
        ),
    ]

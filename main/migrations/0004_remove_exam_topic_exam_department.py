# Generated by Django 4.2 on 2023-05-11 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='topic',
        ),
        migrations.AddField(
            model_name='exam',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exams_department', to='main.department'),
        ),
    ]

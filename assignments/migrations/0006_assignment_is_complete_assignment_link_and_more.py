# Generated by Django 5.0 on 2023-12-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_alter_course_options_course_format_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assignment',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='total_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
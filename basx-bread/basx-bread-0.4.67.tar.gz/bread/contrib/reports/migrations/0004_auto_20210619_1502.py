# Generated by Django 3.1.7 on 2021-06-19 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0003_report_custom_queryset"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="custom_queryset",
            field=models.CharField(
                blank=True,
                help_text="Key in 'settings.REPORT_FILTERS' must be a function returning a queryset",
                max_length=255,
                verbose_name="Custom Filter",
            ),
        ),
    ]

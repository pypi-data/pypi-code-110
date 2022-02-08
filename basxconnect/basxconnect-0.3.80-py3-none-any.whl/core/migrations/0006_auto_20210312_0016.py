# Generated by Django 3.1.5 on 2021-03-11 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20210311_1851"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalnaturalperson",
            name="type",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                limit_choices_to={"category__slug": "naturaltype"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="core.term",
            ),
        ),
        migrations.AddField(
            model_name="naturalperson",
            name="type",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"category__slug": "naturaltype"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.term",
            ),
        ),
    ]

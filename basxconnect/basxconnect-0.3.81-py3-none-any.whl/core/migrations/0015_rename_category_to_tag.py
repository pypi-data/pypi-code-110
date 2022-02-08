# Generated by Django 3.2.5 on 2021-09-28 08:15

from django.db import migrations
from django.utils.translation import gettext_lazy as _


class Migration(migrations.Migration):
    def rename(apps, schema_editor):
        Vocabulary = apps.get_model("core.Vocabulary")
        tag = Vocabulary.objects.filter(slug="category").first()
        if tag is not None:
            tag.slug = "tag"
            tag.name = _("Tag")
            tag.save()

    def rename_undo(apps, schema_editor):
        Vocabulary = apps.get_model("core.Vocabulary")
        tag = Vocabulary.objects.filter(slug="tag").first()
        if tag is not None:
            tag.slug = "category"
            tag.slug = _("Category")
            tag.save()

    dependencies = [
        ("core", "0014_auto_20210928_1512"),
    ]

    operations = [migrations.RunPython(rename, rename_undo)]

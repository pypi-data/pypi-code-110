# Generated by Django 3.2.9 on 2021-11-06 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper_uploads_cloudinary', '0003_delete_cloudinarycollection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cloudinaryfileitem',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='cloudinaryimageitem',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='cloudinarymediaitem',
            options={'default_permissions': ()},
        ),
    ]

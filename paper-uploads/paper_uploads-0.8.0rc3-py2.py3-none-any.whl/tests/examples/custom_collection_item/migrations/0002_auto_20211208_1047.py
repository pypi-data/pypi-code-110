# Generated by Django 3.2.9 on 2021-12-08 10:47

from django.db import migrations
import django.db.models.deletion
import django.db.models.manager
import paper_uploads.models.fields.collection


class Migration(migrations.Migration):

    dependencies = [
        ('paper_uploads', '0007_alter_collection_options'),
        ('custom_collection_item', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollectionDefinition',
        ),
        migrations.CreateModel(
            name='CustomImageCollection',
            fields=[
            ],
            options={
                'proxy': True,
                'default_permissions': (),
                'indexes': [],
                'constraints': [],
            },
            bases=('paper_uploads.imagecollection',),
            managers=[
                ('default_mgr', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='gallery',
            field=paper_uploads.models.fields.collection.CollectionField(on_delete=django.db.models.deletion.SET_NULL, to='custom_collection_item.customimagecollection', verbose_name='gallery'),
        ),
    ]

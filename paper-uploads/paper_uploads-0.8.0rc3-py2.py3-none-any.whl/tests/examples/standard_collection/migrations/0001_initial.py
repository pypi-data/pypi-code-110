# Generated by Django 3.2.9 on 2021-12-02 18:28

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import paper_uploads.models.fields.collection


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paper_uploads', '0007_alter_collection_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardCollection',
            fields=[
            ],
            options={
                'proxy': True,
                'default_permissions': (),
                'indexes': [],
                'constraints': [],
            },
            bases=('paper_uploads.collection',),
            managers=[
                ('default_mgr', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', paper_uploads.models.fields.collection.CollectionField(on_delete=django.db.models.deletion.SET_NULL, to='standard_collection.standardcollection', verbose_name='collection')),
            ],
            options={
                'verbose_name': 'Page',
            },
        ),
    ]

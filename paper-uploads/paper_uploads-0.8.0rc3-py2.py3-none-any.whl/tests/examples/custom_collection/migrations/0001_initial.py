# Generated by Django 3.2.9 on 2021-12-02 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import paper_uploads.models.fields.collection


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paper_uploads', '0007_alter_collection_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCollection',
            fields=[
                ('collection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='paper_uploads.collection')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'proxy': False,
                'default_permissions': (),
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
                ('gallery', paper_uploads.models.fields.collection.CollectionField(on_delete=django.db.models.deletion.SET_NULL, to='custom_collection.customcollection', verbose_name='gallery')),
            ],
            options={
                'verbose_name': 'Page',
            },
        ),
    ]

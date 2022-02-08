# Generated by Django 3.2.9 on 2021-12-02 20:06

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import paper_uploads.models.fields.collection
import paper_uploads.models.fields.image
import paper_uploads.models.mixins
import paper_uploads.models.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paper_uploads', '0007_alter_collection_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionDefinition',
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
                ('gallery', paper_uploads.models.fields.collection.CollectionField(on_delete=django.db.models.deletion.SET_NULL, to='custom_collection_item.collectiondefinition', verbose_name='gallery')),
            ],
            options={
                'verbose_name': 'Page',
            },
        ),
        migrations.CreateModel(
            name='CustomImageItem',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='changed at')),
                ('basename', models.CharField(editable=False, help_text='Human-readable resource name', max_length=255, verbose_name='basename')),
                ('extension', models.CharField(editable=False, help_text='Lowercase, without leading dot', max_length=32, verbose_name='extension')),
                ('size', models.PositiveIntegerField(default=0, editable=False, verbose_name='size')),
                ('checksum', models.CharField(editable=False, max_length=64, verbose_name='checksum')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='uploaded at')),
                ('title', models.CharField(blank=True, help_text='The title is being used as a tooltip when the user hovers the mouse over the image', max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='This text will be used by screen readers, search engines, or when the image cannot be loaded', verbose_name='description')),
                ('width', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='width')),
                ('height', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='height')),
                ('cropregion', models.CharField(blank=True, editable=False, max_length=24, verbose_name='crop region')),
                ('file', paper_uploads.models.fields.image.VariationalFileField(max_length=255, storage=django.core.files.storage.FileSystemStorage(), upload_to=paper_uploads.models.utils.generate_filename, verbose_name='file')),
                ('collectionitembase_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='paper_uploads.collectionitembase')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
            },
            bases=('paper_uploads.collectionitembase', paper_uploads.models.mixins.FileFieldProxyMixin, paper_uploads.models.mixins.FileProxyMixin, models.Model),
        ),
    ]

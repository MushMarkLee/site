# Generated by Django 3.1.6 on 2021-02-12 16:36

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0003_auto_20210212_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworks',
            name='img',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='D:/work2/maria/maria/artworks/static/artworks/media'), upload_to='artworks/static/artworks/media'),
        ),
    ]

# Generated by Django 2.1.2 on 2018-11-14 07:00

from django.db import migrations
import private_storage.fields
import projects.models.project


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_image_to_file_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectattributefile',
            name='file',
            field=private_storage.fields.PrivateFileField(storage=projects.models.project.OverwriteStorage(), upload_to='', verbose_name='File'),
        ),
    ]
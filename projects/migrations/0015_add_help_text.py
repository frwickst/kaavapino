# Generated by Django 2.0.1 on 2018-02-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='help_text',
            field=models.TextField(blank=True, null=True, verbose_name='Help text'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value_type',
            field=models.CharField(choices=[('integer', 'integer'), ('short_string', 'short string'), ('long_string', 'long string'), ('boolean', 'boolean'), ('date', 'date'), ('user', 'user')], max_length=64, verbose_name='value type'),
        ),
    ]

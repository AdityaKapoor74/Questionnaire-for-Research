# Generated by Django 2.2.6 on 2020-02-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllTogether', '0005_auto_20200210_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponsesfordescription',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]

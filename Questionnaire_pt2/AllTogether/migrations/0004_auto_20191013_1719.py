# Generated by Django 2.2.6 on 2019-10-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllTogether', '0003_remove_userdetails_stimuli_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text_for_real_test',
            field=models.CharField(max_length=300),
        ),
    ]

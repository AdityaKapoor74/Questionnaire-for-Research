# Generated by Django 2.2.3 on 2019-08-04 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample1_A', models.ImageField(upload_to='images/')),
                ('sample2_A', models.ImageField(upload_to='images/')),
                ('sample3_A', models.ImageField(upload_to='images/')),
                ('sample4_A', models.ImageField(upload_to='images/')),
                ('sample5_A', models.ImageField(upload_to='images/')),
                ('sample1_B', models.ImageField(upload_to='images/')),
                ('sample2_B', models.ImageField(upload_to='images/')),
                ('sample3_B', models.ImageField(upload_to='images/')),
                ('sample4_B', models.ImageField(upload_to='images/')),
                ('sample5_B', models.ImageField(upload_to='images/')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
    ]

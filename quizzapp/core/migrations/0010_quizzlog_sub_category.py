# Generated by Django 3.2.8 on 2021-12-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20211203_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizzlog',
            name='sub_category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

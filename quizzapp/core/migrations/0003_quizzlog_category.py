# Generated by Django 3.2.9 on 2021-12-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_usertotalscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizzlog',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

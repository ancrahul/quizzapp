# Generated by Django 3.2.9 on 2021-12-06 14:31

import annoying.fields
from django.conf import settings
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_alter_usertotalscore_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertotalscore',
            name='id',
        ),
        migrations.AlterField(
            model_name='usertotalscore',
            name='user',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

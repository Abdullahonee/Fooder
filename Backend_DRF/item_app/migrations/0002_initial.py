# Generated by Django 4.1 on 2022-08-20 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemlist', to=settings.AUTH_USER_MODEL),
        ),
    ]

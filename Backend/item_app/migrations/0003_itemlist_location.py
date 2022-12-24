# Generated by Django 4.1 on 2022-11-14 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_locationdist_remove_locations_distance_and_more'),
        ('item_app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='location.locationdist'),
            preserve_default=False,
        ),
    ]

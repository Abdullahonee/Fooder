# Generated by Django 4.1 on 2022-08-20 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('is_confirmed', models.BooleanField(default=True)),
                ('extra', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlist', to='item_app.itemlist')),
            ],
        ),
    ]
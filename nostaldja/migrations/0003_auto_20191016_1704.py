# Generated by Django 2.2.6 on 2019-10-16 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0002_auto_20191016_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fad',
            name='decade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.Decade'),
        ),
    ]

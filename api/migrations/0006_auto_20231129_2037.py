# Generated by Django 3.2.19 on 2023-11-29 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20231127_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='dron',
        ),
        migrations.AddField(
            model_name='drug',
            name='dron',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.dron'),
        ),
    ]

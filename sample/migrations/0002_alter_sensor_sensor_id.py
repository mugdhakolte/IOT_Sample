# Generated by Django 4.0.5 on 2022-06-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
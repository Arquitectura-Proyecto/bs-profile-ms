# Generated by Django 2.2.12 on 2020-04-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_speciality_trainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='degree_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

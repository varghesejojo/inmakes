# Generated by Django 4.0.2 on 2023-06-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slnumber', models.IntegerField()),
                ('itemname', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]

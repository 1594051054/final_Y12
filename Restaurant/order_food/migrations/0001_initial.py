# Generated by Django 2.0.1 on 2018-04-19 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(blank=True, max_length=180, null=True)),
                ('address', models.CharField(blank=True, max_length=180, null=True)),
            ],
        ),
    ]

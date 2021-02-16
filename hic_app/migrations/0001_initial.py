# Generated by Django 3.1.6 on 2021-02-12 23:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('address', models.TextField()),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/hospital/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hic_app.hospital_type')),
            ],
        ),
    ]

# Generated by Django 3.0 on 2019-12-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest_server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'file',
            },
        ),
    ]

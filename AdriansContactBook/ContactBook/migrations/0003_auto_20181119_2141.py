# Generated by Django 2.1.3 on 2018-11-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactBook', '0002_auto_20181119_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='nick',
            field=models.CharField(default='empty', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=128),
        ),
    ]
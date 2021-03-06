# Generated by Django 2.1.5 on 2019-04-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0003_auto_20190421_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='college',
        ),
        migrations.AddField(
            model_name='college',
            name='faculty',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='college',
            name='fees',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='college',
            name='genders',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='college',
            name='location',
            field=models.CharField(default='null', max_length=1000),
        ),
        migrations.AddField(
            model_name='college',
            name='size',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='college',
            name='students',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='college',
            name='affliation',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(default='null', max_length=250),
        ),
        migrations.AlterField(
            model_name='college',
            name='college_pic',
            field=models.CharField(default='null', max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='college_website',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]

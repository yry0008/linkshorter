# Generated by Django 3.2.10 on 2021-12-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='del_token',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='link',
            name='redirect',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='link',
            name='token',
            field=models.CharField(default='', max_length=200),
        ),
    ]
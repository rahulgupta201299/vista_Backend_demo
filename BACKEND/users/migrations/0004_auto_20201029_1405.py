# Generated by Django 3.1.2 on 2020-10-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201029_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='useradd',
            name='address',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='useradd',
            name='std',
            field=models.IntegerField(default='8'),
        ),
        migrations.AddField(
            model_name='useradd',
            name='upload',
            field=models.FileField(default='Empty', upload_to=''),
        ),
        migrations.AlterField(
            model_name='useradd',
            name='phone_no',
            field=models.CharField(default='0000000000', max_length=255),
        ),
    ]
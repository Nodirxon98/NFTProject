# Generated by Django 4.2.7 on 2023-11-15 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_usermodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

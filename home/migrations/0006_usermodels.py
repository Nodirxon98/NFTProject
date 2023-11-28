# Generated by Django 4.2.7 on 2023-11-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_usermodels_alter_usermodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='defult_avatar_png', null=True, upload_to='images/')),
            ],
        ),
    ]
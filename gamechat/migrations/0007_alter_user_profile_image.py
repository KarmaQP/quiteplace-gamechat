# Generated by Django 4.0.4 on 2022-04-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamechat', '0006_alter_message_date_alter_message_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='images/avatar.jpg', upload_to='images'),
        ),
    ]

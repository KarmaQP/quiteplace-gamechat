# Generated by Django 4.0.4 on 2022-04-25 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamechat', '0004_role_remove_user_role_alter_user_username_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='roles', to='gamechat.role'),
        ),
    ]

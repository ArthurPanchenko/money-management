# Generated by Django 5.0.4 on 2024-05-09 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0009_alter_purchase_options_wallet_avaiable_today_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='avaiable_today',
            new_name='available_today',
        ),
    ]

# Generated by Django 4.2 on 2023-04-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_email_accounts_details_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_accounts_details',
            name='flickr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='email_accounts_details',
            name='four_square',
            field=models.TextField(null=True),
        ),
    ]
# Generated by Django 4.2 on 2023-04-08 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_email_accounts_details_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_accounts_details',
            name='facebook',
            field=models.TextField(null=True),
        ),
    ]

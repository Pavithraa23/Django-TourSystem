# Generated by Django 5.1.1 on 2024-10-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0010_rename_comment_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

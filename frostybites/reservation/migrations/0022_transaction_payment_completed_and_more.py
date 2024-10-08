# Generated by Django 5.0.4 on 2024-05-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0021_remove_reservation_username_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='pending', max_length=20),
        ),
    ]

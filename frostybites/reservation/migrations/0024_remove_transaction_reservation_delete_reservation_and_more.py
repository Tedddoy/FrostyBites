# Generated by Django 5.0.4 on 2024-10-02 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0023_remove_transaction_payment_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='reservation',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]

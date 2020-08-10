# Generated by Django 3.1 on 2020-08-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('COD', 'Cash On Delivery'), ('PAYPAL', 'paypal')], default='COD', max_length=50, verbose_name='Payment Method'),
        ),
    ]
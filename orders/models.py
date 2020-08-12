from django.db import models
from django.db import models
from django_countries.fields import CountryField
from ecommerce.models import Product


class Order(models.Model):
    PAYMENT_METHOD = (
        ('COD', 'Cash On Delivery'),
        ('PAYPAL', 'paypal'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=250)
    country = CountryField(blank_label='(select country)')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50, default='Punjab')
    postal_code = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    additional_information = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(choices=PAYMENT_METHOD,
                                      verbose_name="Payment Method", max_length=50, blank=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)


class OrderItem(models.Model):
    TAX_RATE = 0.05
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.FloatField(default=300)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)



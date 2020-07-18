from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from taggit.managers import TaggableManager
from comments . models import Comment


CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

FEATURE_CHOICES = (
    ('none', 'None'),
    ('featured_accessories', 'Featured Accessories'),
    ('featured_bags', 'Featured Bags'),
    ('featured_clothing', 'Featured Clothing'),
    ('featured_footwear', 'Featured Footwear'),


)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class Category(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        unique_together = ['name', 'slug']
        ordering = ['name']
        verbose_name_plural = 'categories'

    def get_category_url(self):
        return reverse("core:categoryview", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.name

    @property
    def get_category_count(self):
        return self.item_set.all().count()


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    new_arrival = models.BooleanField(default=False, blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    discount_percent = models.FloatField(blank=True,  null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1,)
    label = models.CharField(choices=FEATURE_CHOICES, max_length=1000)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    image_1 = models.ImageField(blank=True,  null=True)
    image_2 = models.ImageField(blank=True,  null=True)
    image_3 = models.ImageField(blank=True,  null=True)
    image_4 = models.ImageField(blank=True,  null=True)

    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['title', 'slug']

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

    @property
    def get_review_count(self):
        return self.reviews_set.all().count()

    @property
    def reviews(self):
        return self.reviews_set.all()

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100, blank=False)
    apartment_address = models.CharField(max_length=100, blank=False)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, blank=False, null=True)
    state = models.CharField(max_length=120, blank=False, null=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    reference = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15, default='None')
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


class Slider(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField()

    def __str__(self):
        return self.title


class HomepageBanner(models.Model):
    image = models.ImageField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Image"


class HomesideBanner(models.Model):
    image = models.ImageField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Image"


class ShoptopBanner(models.Model):
    image = models.ImageField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Image"


class ShopbottomBanner(models.Model):
    image = models.ImageField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Image"


class Reviews(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    review = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Reviews'


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

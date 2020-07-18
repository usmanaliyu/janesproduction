from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paystack')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_phone = forms.CharField(required=False)
    shipping_state = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='Select Country').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_phone = forms.CharField(required=False)
    billing_state = forms.CharField(required=False)
    billing_country = CountryField(blank_label='Select Country').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))

    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)


class CouponForm(forms.Form):
    code = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


class ReviewForm(forms.Form):
    review = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        "row": 10,
        'resize': "none",
        'label': 'Comment'
    }))


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    subject = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(max_length=300, required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'resize': 'none'
    }))


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

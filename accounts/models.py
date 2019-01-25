from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

# from OnlineShop import settings
# from accounts.managers import CustomUserManager
from products.models import Product


# import stripe
#
# stripe.api_key = settings.STRIPE_SECRET_KEY


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    purchased_products = models.ManyToManyField(Product, blank=True)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = Profile.objects.get_or_create(user=instance)

    # if user_profile.stripe_id is None or user_profile.stripe_id == '':
    #     new_stripe_id = stripe.Customer.create(email=instance.email)
    #     user_profile.stripe_id = new_stripe_id['id']
    #     user_profile.save()


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)



# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import gettext_lazy as _
#
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, null=True)
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this admin site.'),
#     )
#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. ''Unselect this instead of deleting accounts.'
#         ),
#     )
#
#     USERNAME_FIELD = 'email'
#     objects = CustomUserManager()
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#
#     def get_full_name(self):
#         return self.email
#
#     def get_short_name(self):
#         return self.get_full_name()
#
#     def __str__(self):
#         return self.email
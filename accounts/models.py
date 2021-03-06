from django.conf import settings
from django.contrib.auth.models import User
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



class EmailAuthBackend():
    def authenticate(self,request,username,password):
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                success = user.check_password(password)

                if success:
                    return user
            except User.DoesNotExist:
                pass
            return None

        try:
            user = User.objects.get(username=username)
            success = user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None

    def get_user(self,uid):
        try:
            return User.objects.get(pk=uid)
        except:
            return None

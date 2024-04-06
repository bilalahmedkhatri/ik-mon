from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

from datetime import datetime
# Create your models here.


class MainUser(AbstractUser):

    def user_profile_photo(instance, file_upload):
        print("test dir: ", instance)
        date_time = datetime.now()
        char = get_random_string(length=10)
        file_extension = file_upload.split('.')[1]
        file_upload = f"{date_time.day}_{char}.{file_extension}"
        path = "user_profile_photos/" + file_upload
        return path

    user_profile_pic = models.ImageField(
        upload_to=user_profile_photo, blank=True, null=True)
    contact = models.IntegerField(default=12345678, verbose_name="Contact")
    website = models.CharField(
        max_length=20, default="teamstellar.com", verbose_name="Website")
    location = models.CharField(
        max_length=70, verbose_name="Location", default="karachi")
    doi = models.DateField(auto_now=False, blank=True,
                           default="2022-01-01", verbose_name="Date of Incorporation")
    type_of_work = models.CharField(
        max_length=50, default='Social Service', verbose_name="Type of work")

    # USERNAME_FIELD = ["phone_no"]

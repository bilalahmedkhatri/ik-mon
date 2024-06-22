from collections.abc import Sequence
from django.contrib import admin
from django.http.request import HttpRequest
from accounts.models import MainCustomUser

# Register your models here.


@admin.register(MainCustomUser)
class AdminUserMonitor(admin.ModelAdmin):
    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        return super(AdminUserMonitor, self).get_list_display(request)


# est values [ admin.logentry>,  authtoken.token>,  account.emailaddress>,  socialaccount.socialaccount>,  id>,   password>,   last_login>,  is_superuser>,   username>,   first_name>,   last_name>,  EmailField: email>,  is_staff>,  is_active>,   date_joined>,    user_profile_pic>, contact>,   website>,   location>,
# doi>,   type_of_work>, groups>, user_permissions>]
# test values [ admin.logentry>,  authtoken.token>,  account.emailaddress>,  socialaccount.socialaccount>,  id>,   password>,   last_login>,  is_superuser>,   username>,   first_name>,   last_name>,  EmailField: email>,  is_staff>,  is_active>,   date_joined>,    user_profile_pic>, contact>,   website>,   location>,
# doi>,   type_of_work>, groups>, user_permissions>]

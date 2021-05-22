from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Override the default behaviour
UserAdmin.add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )

# Custom Panel Features
class AccountAdmin(UserAdmin):
    list_display = (
        'username','date_joined','last_login','is_superuser','is_staff'
    )
    # we can search for these in admin panel
    search_fields = ('username',)
    # these cannot be changed from admin page
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () # required

# Register Model and Manager
admin.site.register(Account,AccountAdmin)

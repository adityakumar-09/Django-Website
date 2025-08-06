from django.contrib import admin

from .models import Product,Orders,Contact
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
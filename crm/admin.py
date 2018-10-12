from django.contrib import admin

# Register your models here.
from .models import Document, Company, Users, Leads
admin.site.register(Document)
admin.site.register(Company)
admin.site.register(Users)
admin.site.register(Leads)
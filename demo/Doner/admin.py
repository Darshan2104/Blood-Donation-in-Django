from django.contrib import admin
from .models import Donerinfo, ReqDonerinfo, BloodBankinfo, Hospital

# Register your models here.
admin.site.register(Donerinfo)
admin.site.register(ReqDonerinfo)
admin.site.register(BloodBankinfo)
admin.site.register(Hospital)

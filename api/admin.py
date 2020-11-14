from django.contrib import admin

# Register your models here.
from api.models import MMCModel


class MMCModelAdmin(admin.ModelAdmin):
    # readonly_fields = ('id',)
    list_display = ['c_value', 'lambda_value', 'mu_value', 'l_value', 'lq_value',
                    'w_value', 'wq_value', 'rho_value', 'p0_value']


admin.site.register(MMCModel, MMCModelAdmin)

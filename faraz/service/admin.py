from django.contrib import admin
from .models import person , customer , recive_cheque , contract , product , karbarg , msg

# Register your models here.



class recive_chequeInline(admin.TabularInline):
    model = recive_cheque



class contractAdmin(admin.ModelAdmin):
    list_filter = ['date']
    inlines = [
    recive_chequeInline,
    ]


admin.site.register(karbarg)
admin.site.register(person)
admin.site.register(customer)
admin.site.register(recive_cheque)
admin.site.register(contract , contractAdmin)
admin.site.register(product)
admin.site.register(msg)
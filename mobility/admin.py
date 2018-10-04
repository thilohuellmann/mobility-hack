from django.contrib import admin

# class SubscriptionAdmin(admin.ModelAdmin):
#     list_display = ('email','plan','status','current_period_start','current_period_end')
#
# class credit_cardAdmin(admin.ModelAdmin):
#     list_display = ('email','brand','last4','exp_month','exp_year')
#
# class customerAdmin(admin.ModelAdmin):
#     list_display = ('email','user_id','stripe_id')
#
# class invoiceAdmin(admin.ModelAdmin):
#     list_display = ('email','plan','total','created_on','invoice_url')
#
# class UsageAdmin(admin.ModelAdmin):
#     list_display = ('email','user_id','usage_volume','volume_used')
#
# class FileAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'file_name', 'classes', 'file_type', 'has_header', 'gamification_enabled', 'chunks', 'completed_rows', 'total_rows')
#
# admin.site.register(File) #, FileAdmin
# admin.site.register(Subscription, SubscriptionAdmin)
# admin.site.register(credit_card, credit_cardAdmin)
# admin.site.register(customer, customerAdmin)
# admin.site.register(invoice, invoiceAdmin)
# admin.site.register(Usage, UsageAdmin)

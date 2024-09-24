from django.contrib import admin
from .models import (
    Order, OrderLineItem, CustomersEnrolledOnCourse, ClassAttendance
)


# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total', )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, )

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city',
              'street_address1', 'street_address2',
              'county', 'delivery_cost',
              'order_total', 'grand_total',
              'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


class CustomersEnrolledOnCourseAdmin(admin.ModelAdmin):
    list_display = (
        'order_line_item',
        'wo_program',
        'date',
    )


class ClassAttendanceAdmin(admin.ModelAdmin):
    """ Allows ClassAttendances to be viewed in Admin """

    lis_display = (
        'workout_program',
        'student',
        'date',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(CustomersEnrolledOnCourse, CustomersEnrolledOnCourseAdmin)
admin.site.register(ClassAttendance, ClassAttendanceAdmin)

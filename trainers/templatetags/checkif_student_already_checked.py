from django import template

register = template.Library()


@register.filter(name='check_already_checked')
def check_already_checked(student, class_already_taken):
    for stud_entry in class_already_taken:
        stud = str(stud_entry.student.order_line_item.order.full_name)
        if stud == str(student):
            return True
    return False

from django import template


register = template.Library()

@register.filter(name='check_already_checked')
def check_already_checked(student, class_already_taken):
    print(f"S:{student}")
    for stud_entry in class_already_taken:
        print(f"stud_entry:{stud_entry}")
        if str(stud_entry.student.order_line_item.order.full_name) == str(student):
            print("match")
            return True
    return False

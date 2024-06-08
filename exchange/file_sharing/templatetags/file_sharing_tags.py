from django import template
from django.http import request

from file_sharing.models import *

register = template.Library()


# функция для простого тега
@register.simple_tag(name='getdisciplines')
def get_disciplines(filter=None):
    if not filter:
        return Discipline.objects.all()
    else:
        return Discipline.objects.filter(pk=filter)


# @register.inclusion_tag('file_sharing/list_disciplines.html')
# def show_disciplines(sort=None, discipline_selected=0):
#     user = request.user
#
#     # Получаем записи, в которых текущий пользователь есть в поле group
#     records = Record.objects.filter(group=user.group).select_related('discipline')
#     print(records)
#     if not sort:
#         disciplines = Discipline.objects.all()
#     else:
#         disciplines = Discipline.objects.order_by(sort)
#     return {"disciplines": disciplines, 'discipline_selected': discipline_selected}

@register.inclusion_tag('file_sharing/list_disciplines.html')
def show_disciplines(sort=None, discipline_selected=0):
    if not sort:
        disciplines = Discipline.objects.all()
    else:
        disciplines = Discipline.objects.order_by(sort)
    return {"disciplines": disciplines, 'discipline_selected': discipline_selected}


@register.filter
def file_extension(file_name):
    extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.jpg', '.jpeg', '.png', '.pptx', '.jfif', '.txt', '.rar']
    for extension in extensions:
        if file_name.endswith(extension):
            return extension
    return None

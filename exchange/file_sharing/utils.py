from django.db.models import Count
from django.core.cache import cache

from file_sharing.models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Полезные контакты", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):

        context = kwargs

        if self.request.user.is_authenticated:
            user = self.request.user
            records = Record.objects.filter(group=user.group)
            discipline_ids = records.values_list('discipline',
                                                 flat=True).distinct()
            disciplines = Discipline.objects.filter(pk__in=discipline_ids)
        else:
            disciplines = Discipline.objects.all()

        context['menu'] = menu
        context['disciplines'] = disciplines
        if 'discipline_selected' not in context:
            context['discipline_selected'] = 0
        return context

    # def get_user_context(self, **kwargs):
    #     context = kwargs
    #     # подключаем механизм кеширования
    #     # disciplines = cache.get('disciplines')
    #     # if not disciplines:
    #     #     disciplines = Discipline.objects.all()
    #     #     cache.set('disciplines', disciplines, 60)
    #
    #     # без кеширования
    #     disciplines = Discipline.objects.all() #так было ДО кеширования
    #     context['menu'] = menu
    #     context['disciplines'] = disciplines
    #     if 'discipline_selected' not in context:
    #         context['discipline_selected'] = 0
    #     return context

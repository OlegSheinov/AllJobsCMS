from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Orderable
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail_color_panel.fields import ColorField


class Rank(Orderable):
    name = models.CharField(
        max_length=255,
        verbose_name='Название ранга заявки'
    )
    color = ColorField()
    is_default = models.BooleanField(
        default=False,
        verbose_name='Является рангом по-умолчанию',
        help_text='Новым заявкам будет проставляться данный ранг (если не указан какой-либо другой)',
        blank=True
    )

    panels = [
        FieldPanel("name"),
        NativeColorPanel("color"),
        FieldPanel("is_default"),
    ]

    def __str__(self):
        return self.name

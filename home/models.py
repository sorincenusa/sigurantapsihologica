from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks

class HomePage(Page):
    hero_title = models.CharField(
        max_length=255,
        default="Impactul siguranței psihologice asupra performanței și inovației",
        help_text="Mesajul principal clar."
    )
    hero_subtitle = models.TextField(
        default="O cultură a învățării înlocuiește cultura vinovăției. Află cum poți construi echipe performante.",
        help_text="Subtitlul explicativ."
    )

    philosophy_statement = RichTextField(
        default="<p>Siguranța psihologică nu este un lux, ci o necesitate strategică asumată de la nivel de management.</p>",
        help_text="Declarația despre rolul managementului în siguranța psihologică."
    )

    services = StreamField([
        ('service', blocks.StructBlock([
            ('title', blocks.CharBlock(required=True)),
            ('description', blocks.TextBlock(required=True)),
        ], icon='cog')),
    ], use_json_field=True, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('philosophy_statement'),
        FieldPanel('services'),
    ]

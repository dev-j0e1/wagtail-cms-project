from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from core.blocks import HomeTitleBlock
from core.blocks import HeroBlock
from core.blocks import HighlightsBlock
from core.blocks import AboutBlock
from core.blocks import CallToActionBlock



class HomePage(Page):
    templates = "home/home_page.html"
    body = RichTextField(blank=True)

    test_body = StreamField([
        ("home_title_block", HomeTitleBlock()),
        ("hero_block", HeroBlock()),
        ("highlights_block", HighlightsBlock()),
        ("about_block", AboutBlock()),
        ("call_to_action_block", CallToActionBlock())

        

    ], use_json_field=True, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"), 
        FieldPanel("test_body")
    ]

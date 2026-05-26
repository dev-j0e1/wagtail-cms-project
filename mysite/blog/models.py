from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class BlogIndexPage(Page):

    template = "blog/blog_index_page.html"

    subpage_types = ['blog.BlogPage']

    def get_context(self, request):
        context = super().get_context(request)

        context['posts'] = (
            BlogPage.objects
            .child_of(self)
            .live()
            .order_by('-publication_date')
        )

        return context

class BlogPage(Page):

    template = "blog/blog_page.html"

    publication_date = models.DateField()

    summary = models.TextField()

    body = RichTextField()

    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('publication_date'),
        FieldPanel('summary'),
        FieldPanel('body'),
        FieldPanel('featured_image'),
    ]
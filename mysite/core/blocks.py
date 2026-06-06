from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class HeroBlock(blocks.StructBlock):
    background_image = ImageChooserBlock(required=False, help_text="This will be the background image of a block")
    header_text = blocks.CharBlock(required=True, help_text="This is a header text")

    class Meta:
        template = "blocks/hero_block.html"

class HighlightsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="This is the title text")
    highlights = blocks.ListBlock(
        blocks.StructBlock([
            ("title", blocks.CharBlock(required=True, help_text="Highlight title")),
            ("body", blocks.RichTextBlock(required=True, help_text="Highlight body")),
        ]),
        min_num=1,
        help_text="Add at least three highlights (each with a title and body)",
    )
    class Meta:
        template = "blocks/highlights_block.html"

class AboutBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="This is the title for the about block")
    subtitle = blocks.CharBlock(required=True, help_text="This is the subtitle for the about block")
    features = blocks.ListBlock(
        blocks.StructBlock([
            ("text", blocks.CharBlock(required=True, help_text="This is a listed feature")),
        ]),
        help_text="Add the features of this project",
    )
    class Meta:
        template = "blocks/about_block.html"

class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="This is the title for the call to action block")
    subtitle = blocks.CharBlock(required=True, help_text="This is the subtitle for the call to action block")
    button_name = blocks.CharBlock(required=True, help_text="This is the name for the call to action button")

    class Meta:
        template = "blocks/call_to_action_block.html"

class HomeTitleBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="This is the title for the home page")

    class Meta:
        template = "blocks/home_title_block.html"
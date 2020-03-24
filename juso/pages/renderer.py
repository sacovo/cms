from django.utils.html import mark_safe
from feincms3 import plugins
from feincms3.renderer import TemplatePluginRenderer

from fomantic_ui import models as fomantic
from juso.utils import render_embed
from juso.plugins import download
from juso.people import plugins as people_plugins
from juso.pages import models as pages

renderer = TemplatePluginRenderer()

renderer.register_string_renderer(
    pages.RichText,
    lambda plugin: plugins.richtext.render_richtext(plugin)
)

renderer.register_string_renderer(
    pages.HTML,
    lambda plugin: plugins.html.render_html(plugin)
)

renderer.register_string_renderer(
    pages.External,
    lambda plugin: render_embed(plugin)
)

renderer.register_string_renderer(
    pages.Image,
    lambda plugin: plugins.image.render_image(plugin)
)

renderer.register_string_renderer(
    pages.Download,
    lambda plugin: download.render_download(plugin)
)

renderer.register_string_renderer(
    pages.Team,
    lambda plugin: people_plugins.render_team(plugin)
)

renderer.register_string_renderer(
    pages.Button,
    lambda plugin: fomantic.render_button(plugin)
)

renderer.register_string_renderer(
    pages.Divider,
    lambda plugin: fomantic.render_divider(plugin)
)

renderer.register_string_renderer(
    pages.Header,
    lambda plugin: fomantic.render_header(plugin)
)

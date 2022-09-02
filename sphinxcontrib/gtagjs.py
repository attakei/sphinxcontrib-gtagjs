"""sphinxcontrib-gtagjs is helper extension to embed gtag.js.

Support HTML based builder.
"""
# flake8: noqa
from typing import Any
from jinja2 import Template
from sphinx.application import Sphinx


__version__ = "0.2.1"


def add_gtagjs_context(
    app: Sphinx, pathname: str, templatename: str, context: dict, doctree: Any
) -> None:
    """Build gtag.js tags and register content.

    TODO: Write tests after
    """
    if len(app.config.gtagjs_ids) == 0:
        return
    template = Template(
        """
        <script async src="https://www.googletagmanager.com/gtag/js?id={{ gtagjs_ids.0 }}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            {% for gtagjs_id in gtagjs_ids %}
            gtag('config', '{{ gtagjs_id }}');
            {% endfor %}
        </script>
    """
    )
    metatags = context.get("metatags", "") + template.render(
        gtagjs_ids=app.config.gtagjs_ids
    )
    context["metatags"] = metatags


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("gtagjs_ids", [], "html")
    app.connect("html-page-context", add_gtagjs_context)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

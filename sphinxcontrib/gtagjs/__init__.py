"""sphinxcontrib-gtagjs is helper extension to embed gtag.js.

Support HTML based builder.
"""
# flake8: noqa
from typing import Any
from jinja2 import Template
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging


__version__ = "0.2.1"

logger = logging.getLogger(__name__)


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


def resolve_static_files(app: Sphinx, config: Config):
    """Inject js files for Google Analytics."""
    if len(app.config.gtagjs_ids) == 0:
        logger.info("'gtagjs_ids' is not set in conf.py")
        return
    gtagjs_url = (
        f"https://www.googletagmanager.com/gtag/js?id={app.config.gtagjs_ids[0]}"
    )
    config.html_js_files.insert(0, gtagjs_url)


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("gtagjs_ids", [], "html")
    app.connect("html-page-context", add_gtagjs_context)
    app.connect("config-inited", resolve_static_files)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

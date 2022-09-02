"""sphinxcontrib-gtagjs is helper extension to embed gtag.js.

Support HTML based builder.
"""
# flake8: noqa
from pathlib import Path
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging


__version__ = "0.2.1"

logger = logging.getLogger(__name__)
static_path = Path(__file__).parent / "_static"


def resolve_static_files(app: Sphinx, config: Config):
    """Inject js files for Google Analytics."""
    if len(app.config.gtagjs_ids) == 0:
        logger.info("'gtagjs_ids' is not set in conf.py")
        return
    gtagjs_url = (
        f"https://www.googletagmanager.com/gtag/js?id={app.config.gtagjs_ids[0]}"
    )
    # NOTE: Now supporting only html or dirhtml
    # Putting to head of list, for declare gtagjs events by user's js
    config.html_js_files = [
        gtagjs_url,
        "sphinxcontrib.gtagjs.js",
    ] + config.html_js_files
    app.config.html_static_path.append(str(static_path))
    app.config.html_context["gtagjs_ids"] = app.config.gtagjs_ids


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("gtagjs_ids", [], "html")
    app.connect("config-inited", resolve_static_files)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

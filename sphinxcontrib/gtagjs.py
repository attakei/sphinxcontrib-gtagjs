from sphinx.application import Sphinx


__version__ = "0.0.0"


def setup(app: Sphinx):
    app.add_config_value("gtagjs_ids", [], "html")

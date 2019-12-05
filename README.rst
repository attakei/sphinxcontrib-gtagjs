sphinxcontrib-gtagjs
====================

Sphinx extension to render global site tag of Google.

Installation
------------

Install from PyPI

.. code-block:: bash

    pip install sphinxcontrib-gtagjs

Configuration
-------------

1 - Add this extension into ``conf.py`` .

.. code-block:: python

    extensions = [
        'sphinxcontrib.gtagjs',
    ]

2 - Set your IDs for gtag.js

.. code-block:: python

    gtagjs_ids = [
        'UA-1234-1234',
    ]

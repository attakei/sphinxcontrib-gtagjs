sphinxcontrib-gtagjs
====================

Sphinx extension to render global site tag of Google.

Installation
------------

Currenlty, install from GitHub directly.

.. code-block:: bash

    pip install https://github.com/attakei/sphinxcontrib-gtag/archive/master.zip

Configuration
-------------

1 - Add this extension into ``conf.py`` .

.. code-block:: python

    extensions = [
        'sphinxcontrib.gtag',
    ]

2 - Set your IDs for gtag.js

.. code-block:: python

    gtagjs_ids = [
        'UA-1234-1234',
    ]

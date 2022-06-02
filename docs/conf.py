import sys
from os import path

import tetris

sys.path.insert(0, path.abspath("../tetris"))

project = "python-tetris"
author = 'Sofia "dzshn" N. L.'
copyright = '2021-2022, Sofia "dzshn" N. L.'
author = 'Sofia "dzshn" N. L.'
release = tetris.__version__

extensions = [
    "sphinx.ext.autodoc",
    # "numpydoc",  # TBD, numpydoc is currently too redundant here
    "sphinx.ext.duration",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
default_role = "py:obj"

html_theme = "furo"
html_favicon = "_static/favicon.ico"
html_logo = "_static/logo.png"
html_static_path = ["_static"]

autodoc_member_order = "bysource"
autodoc_type_aliases = {
    "Board": "tetris.types.Board",
    "Minos": "tetris.types.Minos",
    "Seed": "tetris.types.Seed",
}

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "np": ("https://numpy.org/doc/stable", None),
}

python_use_unqualified_type_names = True

# -- Project information -----------------------------------------------------

project = "Guía de Pruebas de Software (STLC)"
copyright = "2025, CIMAT"
author = "Haydeé Hernández"

# título que se ve en la pestaña del navegador
html_title = "Guía de Pruebas de Software"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "myst_parser",     # Markdown
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"

# logo personalizado en la barra lateral
# colocamos tu imagen en docs/_static/logo.png
html_logo = "_static/logo.png"

# Configuración  Furo
html_theme_options = {
    "sidebar_hide_name": False,   # False = muestra el nombre del proyecto junto al logo
    # ajuste de colores:
    # "light_logo": "logo.png",
    # "dark_logo": "logo.png",
}

# Archivos estáticos (CSS, imágenes, etc.)
html_static_path = ["_static"]
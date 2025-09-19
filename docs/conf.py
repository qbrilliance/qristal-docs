# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
# Insert binary output directory where the Pybind11 module is located.
# Note: we use binary rather than install directory so that documentation build can be performed before installation.
sys.path.insert(0, '/gp/git/quantum-brilliance/core/build')
import sphinx_rtd_theme

# -- Google Analytics --

def setup(app):
    app.add_js_file("https://www.googletagmanager.com/gtag/js?id=G-EML76VL6ZZ", loading_method="async")
    app.add_js_file("js/qb_ga.js")

# -- Project information -----------------------------------------------------

project = 'Qristal'
copyright = 'Quantum Brilliance Pty Ltd'
author = 'Quantum Brilliance Pty Ltd'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # breathe and exhale for C++ documentation
    'breathe',
    'exhale',
    # MyST-Parser to handle markdown documentations (e.g., manually written pages)
    # https://www.sphinx-doc.org/en/master/usage/markdown.html
    'myst_parser',
    # Use readthedocs theme
    'sphinx_rtd_theme',
    # Sphinx extensions
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# Excludes the internal README.md file (information about this Documentation build system)
# (Sphinx in strict mode will complain if we have an 'unreachable' markdown document, i.e., not included in any toctree)
exclude_patterns = ['_build', 'html', 'Thumbs.db', '.DS_Store', 'README.md']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# MyST-Parser extensions
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# allow display math (i.e., $$) within an inline context.
# This allows, for example:
# $$ \ket{\Phi^+} = \frac{\ket{00} + \ket{11}}{\sqrt{2}} , $$
# $$ \ket{\Phi^-} = \frac{\ket{00} - \ket{11}}{\sqrt{2}} , $$
# to be displayed as separate paragraphs (no need for empty lines b/w them).
myst_dmath_double_inline = True
myst_heading_anchors = 4

# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`
autosectionlabel_prefix_document = True
autosummary_generate = True
autosummary_imported_members = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False
html_logo = 'static/img/qb_logo.png'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']
html_css_files = [
    'styles/custom.css',
]

# Setup the breathe extension
breathe_projects = {
    "My Project": "/gp/git/quantum-brilliance/core/build/docs/_build/_doxygen/xml"
}
breathe_default_project = "My Project"
breathe_default_members = ('members', 'private-members')

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./_cpp_api",
    "rootFileName":          "library_root.rst",
    "doxygenStripFromPath":  "/gp/git/quantum-brilliance/core/..",
    # Heavily encouraged optional argument (see docs)
    "rootFileTitle":         "C++ API",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    # Files to generate Doxygen docs from
    "exhaleDoxygenStdin":  """INPUT = /gp/git/quantum-brilliance/core/include/qristal/core/circuit_builder.hpp /gp/git/quantum-brilliance/core/include/qristal/core/profiler.hpp /gp/git/quantum-brilliance/core/include/qristal/core/session.hpp /gp/git/quantum-brilliance/core/include/qristal/core/thread_pool.hpp /gp/git/quantum-brilliance/core/include/qristal/core/backends/qb_hardware/qb_qpu.hpp /gp/git/quantum-brilliance/core/include/qristal/core/backends/qb_hardware/qb_visitor.hpp /gp/git/quantum-brilliance/core/include/qristal/core/cudaq/ir_converter.hpp /gp/git/quantum-brilliance/core/include/qristal/core/cudaq/sim_pool.hpp /gp/git/quantum-brilliance/core/include/qristal/core/noise_model/noise_model.hpp /gp/git/quantum-brilliance/core/include/qristal/core/noise_model/noise_properties.hpp /gp/git/quantum-brilliance/core/include/qristal/core/noise_model/readout_error.hpp /gp/git/quantum-brilliance/core/include/qristal/core/optimization/vqee/case_generator.hpp /gp/git/quantum-brilliance/core/include/qristal/core/optimization/vqee/vqee.hpp /gp/git/quantum-brilliance/core/include/qristal/core/passes/base_pass.hpp /gp/git/quantum-brilliance/core/include/qristal/core/passes/noise_aware_placement_config.hpp /gp/git/quantum-brilliance/core/include/qristal/core/passes/noise_aware_placement_pass.hpp /gp/git/quantum-brilliance/core/include/qristal/core/passes/swap_placement_pass.hpp /gp/git/quantum-brilliance/core/include/qristal/core/passes/circuit_opt_passes.hpp /gp/git/quantum-brilliance/emulator/docs/../include/qristal/emulator/emulator.hpp /gp/git/quantum-brilliance/emulator/docs/../include/qristal/emulator/qsim/qsim_emulator.hpp /gp/git/quantum-brilliance/emulator/docs/../include/qristal/emulator/nv_sim/mps_accelerator.hpp /gp/git/quantum-brilliance/emulator/docs/../include/qristal/emulator/noise_model/EmulatorNoiseModel.hpp \n
                              XML_PROGRAMLISTING = NO \n
                              PREDEFINED += __attribute__(x)= \n
                              EXTRACT_PRIVATE = YES"""
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'

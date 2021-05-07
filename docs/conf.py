author = 'quansight'
comments_config = {'hypothesis': False, 'utterances': False}
copyright = '2021'
exclude_patterns = 'docs/**/docs/readme.md _build/* __pycache__/* .nox/* **/.github **/.nox **.ipynb_checkpoints .DS_Store LICENSE Thumbs.db'.split()
execution_allow_errors = False
execution_excludepatterns = []
execution_in_temp = False
execution_timeout = 30
extensions = ['sphinx_togglebutton', 'sphinx_copybutton', 'myst_nb', 'jupyter_book', 'sphinxcontrib.bibtex', 'sphinx_thebe', 'sphinx_comments', 'sphinx.ext.intersphinx', 'sphinx_panels', 'sphinx_book_theme']
extra_extensions = ['sphinx_sitemap']
globaltoc_path = 'docs/toc.yml'
html_add_permalinks = '¶'
html_baseurl = 'https://quansight-writers-workshop.readthedocs.io/en/latest/'
html_favicon = ''
html_logo = ''
html_sourcelink_suffix = ''
html_theme = 'sphinx_book_theme'
html_theme_options = {'search_bar_text': 'Search this book...', 'launch_buttons': {'notebook_interface': 'classic', 'binderhub_url': 'https://mybinder.org', 'jupyterhub_url': '', 'thebe': False, 'colab_url': ''}, 'path_to_docs': '', 'repository_url': 'https://github.com/executablebooks/jupyter-book', 'repository_branch': 'master', 'google_analytics_id': '', 'extra_navbar': '', 'extra_footer': '', 'home_page_in_toc': True, 'use_repository_button': False, 'use_edit_page_button': False, 'use_issues_button': False}
html_title = 'quansight writers workshop'
jupyter_cache = ''
jupyter_execute_notebooks = 'off'
language = None
latex_engine = 'pdflatex'
myst_url_schemes = ['mailto', 'http', 'https']
nb_output_stderr = 'show'
nb_render_priority = {'html': ['application/vnd.jupyter.widget-view+json', 'application/javascript', 'text/html', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/latex', 'text/plain']}
numfig = True
panels_add_bootstrap_css = False
pygments_style = 'sphinx'

master_doc="readme" 
bibtex_bibfiles = []

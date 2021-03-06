"""common tasks for working on the docs folder of project"""

from shutil import which
import shutil, pathlib
from doit.tools import *
jb, tex = which("jb"), which("xelatex")

docs = pathlib.Path("docs")
people = docs / "people"
CONF = pathlib.Path("conf.py")
prepare = "submodule_init config".split()


def task_install_book():
    """install the jupyter book  and sphinx dependencies"""
    if not jb:
        yield dict(
            name="install book deps",
            actions=['pip install --rdocs/requirements.txt'],
            targets=[config_changed(jb)]
        )

def task_install_latex():
    """install the latex dependencies, requires conda"""
    if not tex:
        yield dict(
            name="install latex",
            actions=[
                'mamba install -ycconda-forge texlive-core',
                'sudo apt-get install texlive-latex-recommended texlive-latex-extra \
                     texlive-fonts-recommended texlive-fonts-extra \
                     texlive-xetex latexmk'

            ],
            task_dep=["install_book"],
            uptodate=[config_changed(str(jb))]
        )

def task_html():
    """build the html version of the project"""
    return dict(
        actions=[
            "sphinx-build -j 2 . _build/html",
            "touch _build/html/.nojekyll"
        ],
        targets=["_build/html/index.html"], 
        task_dep=prepare + ["install_book"]
    )

def task_pdf():
    """build the html version of the project"""
    return dict(
        actions=[
            "sphinx-build -j 2 -b latex . _build/latex ",
        ],
        targets=["_build/latex/python.pdf"], 
        task_dep=prepare + ["install_latex"]
    )

def task_submodule_init():
    """configure the content for the short stories"""
    yield dict(
        name="init submodule",
        actions=["git submodule init"]
    )


def task_config():
    def extra_config():
        with open(CONF, "a") as f:
            f.write("""
master_doc="readme" 
bibtex_bibfiles = []
""")
        conf = CONF.read_text()
        CONF.write_text("".join(
            """exclude_patterns = '\
docs/**/docs/readme.md _build/* __pycache__/* .nox/* **/.github **/.nox **.ipynb_checkpoints .DS_Store LICENSE Thumbs.db\
'.split()
""" if x.startswith("exclude_patterns") else x for x in conf.splitlines(True)
        ))
        

    yield dict(
        name="translate jb to sphinx",
        actions=[
            """jb config sphinx --toc docs/toc.yml --config docs/config.yml . > conf.py""",
            extra_config
        ],
        targets=["conf.py"],
        task_dep=["install_book"]
    )
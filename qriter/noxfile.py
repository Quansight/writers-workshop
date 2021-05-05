"""sessions for running tasks to build docs and packages

    nox -s docs
"""
import os
import nox

CI = "GITHUB_ACTION" in os.environ or "READTHEDOCS" in os.environ

@nox.session(reuse_venv=True, python=False if CI else "3.8")
def docs(session):
    session.install(*"""-rworks/requirements-docs.txt --ignore-installed""".split())
    session.run(*"""doit build_docs""".split())

@nox.session(reuse_venv=True, python=False if CI else "3.8", venv_backend="conda")
def pdf(session):
    session.conda_install(
        *"""jupyter-book[sphinx,pdflatex] texlive-core -cconda-forge""".split()
    )
    session.install("bindep")
    session.run("bindep")
    session.run(*"jb build . --toc qww/toc.yml --config qww/config.yml".split())
    session.run(*"jb build . --toc qww/toc.yml --config qww/config.yml --builder pdflatex".split())
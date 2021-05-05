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
import nox
import shutil
import os

extra = dict(python=os.getenv("JUPYTERHUB_CLIENT_ID"))

if extra["python"] is None:
    extra.pop("python")
else:
    extra["python"] = False


@nox.session(reuse_venv=True, venv_backend="conda", **extra)
def docs(session):
    """build the documentation for the writers workshop"""
    session.install("doit")
    session.run(
        *(
            "doit -v1000 html"
            + (" pdf" if "pdf" in session.posargs else "")
        ).split()
    )


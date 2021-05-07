import nox

@nox.session(python="3.8", reuse_venv=True, venv_backend="conda")
def docs(session):
    """build the documentation for the writers workshop"""
    session.install("doit")
    session.run(
        *(
            "doit -v1000 html"
            + (" pdf" if "pdf" in session.posargs else "")
        ).split()
    )


import nox
import shutil

if shutil.which("mamba"):
    # speed things up with mamba if you have it
    if "_run" not in locals():
        _run = nox.sessions.Session._run

    def run(self, *args, **kwargs):
        if args[0] == "conda":
            args = ("mamba",) + args[1:]
        return _run(self, *args, **kwargs)

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


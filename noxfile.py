import nox

def maybe_install(module,  session):
    try:
        session.run(module)
    except nox.command.CommandFailed as e:
        session.install(module)
    

@nox.session(python="3.8", reuse_venv=True, venv_backend="conda")
def docs(session):
    maybe_install("doit", session)

    session.run(
        *(
            "doit v1000 html"
            + (" pdf" if "pdf" in session.posargs else "")
        ).split()
    )


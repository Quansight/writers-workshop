import importlib, pathlib
spec = importlib.util.spec_from_file_location("dodo", pathlib.Path().parent / "docs" / "dodo.py")
module = importlib.util.module_from_spec(spec)
module.__loader__.exec_module(module)
locals().update(vars(module))
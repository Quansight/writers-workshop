import yaml, pathlib        

def task_build_docs():
    return dict(
        actions=[
            "jb build --toc works/toc.yml --config works/config.yml ."
        ],
        targets=["_build/html/index.index.html"]
    )
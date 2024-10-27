from projen.python import PythonProject

project = PythonProject(
    author_email="alexterceros17@gmail.com",
    author_name="alexntg",
    module_name="crud_ualabi",
    name="crud-ualabi",
    version="0.1.0",
)

project.synth()
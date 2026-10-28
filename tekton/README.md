# Tekton setup notes

`pipeline.yaml` is a template, not a ready-to-run pipeline. It assumes a `git-clone` Task is installed and that you create a Task named `accounts-test` that installs `requirements.txt`, runs `flake8 service tests`, and runs `nosetests`. Create a PipelineRun with a workspace binding and your repository URL. For image builds/pushes, configure your cluster's supported build task, registry credentials, and image destination; do not commit registry secrets.

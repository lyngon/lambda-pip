# Python Template
Basic Template for Python projects with Lyngon best-practices and defaults pre-configured.

## Checklist
Do the following things when starting a new project based on this template.

### Python Environment Setup
    to whatever name of the package/service/app.
- Decide which Python version to use . (Example below assumes Python 3.7)
- Run:

    ```
    virtualenv -p python3.7 .venv
    source .venv/bin/activate
    pip install -r src/requirements-dev.txt
    ```

- If applicable: Update the base image in the Dockerfile to reflect the Python version.

### Licence

Unless proprietary:
- Define a licence.
- Populate the `LICENCE` file with the appropriate wording
- Update the `__license__` header meta-data everywhere.. :)
### Project Info
Always:

- Rename the `src/main_package` directory to some relevant name for the app/service.
- Do a global search-and-replace (`Ctrl`+`Shift`+`F` in VS Code) of `main_package` to replace all occurrences with the name of the app/service.

If Docker service: 
- Update the `docker-compose` file with the corresponding service, container and image names.

If package:

- Update the details in `setup.cfg` to reflect the project

### Readme
- Populate this `README` file with something relevant for the project. :)

### Commit the changes to the project repo

### Synthesize AWS CDK stack
```console
cdk synth
```
# Swagger-api-framework

## Combination of API and UI tests which allow lead end-to-end test scenarios

### Set up your environment like described in this guide: https://gist.github.com/KirillY/6a39310b1fea1a8cc7d0d81632426c99

### Install packages and venv
```shell
cd /path/to/project/root
```

### Install dependencies from pyproject.toml
```shell
pdm install
```

### Set up: environment variable configuration

### Create file .env in the yourproject root
```shell
touch .env
```
### Add env's configurations to file .env
```shell
API_URL="http://api.openweathermap.org"
API_KEY="example"
```

### Export environment variables from .env file
```shell
export $(cat .env | xargs)
```

# Usage

### Swagger Documentation `https://swagger.io/docs/open-source-tools/swagger-editor/`

### Example of Run tests which located in the file: `test_api_ui_swagger` :
```shell
pytest -s -v -k test_api_ui_swagger
```

### If you create additional file and aiming to run all files with test scripts:
```shell
pytest -s -v
```

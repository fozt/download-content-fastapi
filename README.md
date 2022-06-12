## Run project using Docker compose
```sh
docker-compose up --build
```

```sh
cd download_content_fastapi
poetry run black .
poetry run isort --sp pyproject.toml .
poetry run flake8 .
```

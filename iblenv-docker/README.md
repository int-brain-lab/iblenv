# `iblenv` Docker

A containerized `iblenv` environment.

## Quick Setup

1. Change to the [docker directory](./): `cd ./iblenv-docker`.

2. Rename `template.env` to `.env`. Set the required environment variables.

3. Run `docker-compose up --detach` ([docker](https://docs.docker.com/get-docker/) and [docker compose](https://docs.docker.com/compose/install/) must be installed).

4. Check if the server is running by going to http://127.0.0.1:8008/lab?token=1blT0k

_See below for more details._

## Docker Build and Run

```bash
cd iblenv-docker/build
PLTARCH=$(uname -m)
GITHUB_USERNAME=iamamutt
docker build \
    --platform=linux/${PLTARCH} \
    --target=iblenv \
    --tag=ghcr.io/${GITHUB_USERNAME}/iblenv:latest \
    --build-arg GITHUB_USERNAME=${GITHUB_USERNAME} \
    --build-arg IMAGE_CREATED=2022-11-11T11:11:11Z \
    --build-arg IMAGE_VERSION=v0.0.0 \
    .
```

```bash
docker run \
    --rm -itdu "root:docker" \
    --name iblenv_local \
    --entrypoint bash \
    ghcr.io/${GITHUB_USERNAME}/iblenv:latest
```

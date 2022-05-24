# syntax=docker/dockerfile:labs

# global arguments shared across different build stages
ARG GITHUB_USERNAME=int-brain-lab
ARG ROOT_ENV_PATH=/int-brain-lab
ARG IMAGE_CREATED=2022-11-11T11:11:11Z
ARG IMAGE_VERSION=v0.0.0

## Stage 1 =============================================================================
## IBL Env Build Stage
## -------------------------------------------------------------------------------------
FROM ghcr.io/${GITHUB_USERNAME}/iblalyx:latest as iblenv_build

ARG ROOT_ENV_PATH

# system environment
ENV TZ="Europe/Lisbon"
ENV LANG=en_US.utf8
ENV LC_ALL=en_US.utf8
ENV LANGUAGE=en_US.utf8
ENV LC_CTYPE=en_US.utf8
ENV QT_QPA_PLATFORM=offscreen

# shell exit on first error within EOF sections
SHELL [ "/bin/bash", "-elc" ]
COPY --chown=999:999 ./ /tmp/

# install debian, conda, and pip packages ----------------------------------------------
USER root:docker
RUN <<-EOF
	xargs </tmp/requirements/apt_requirements.txt apt-get-update-install
	micromamba activate
	micromamba install -yq conda-build
	micromamba install -yq --file /tmp/requirements/conda_requirements.txt
	pip install --no-cache --no-input -vr /tmp/requirements/pip_requirements.txt
	chown 999:999 /usr/local/conda-meta/history /usr/local/pkgs/urls.txt
EOF

# clone repos and add to path ----------------------------------------------------------
USER 999:999
WORKDIR ${ROOT_ENV_PATH}
RUN <<-EOF
	git clone https://github.com/int-brain-lab/iblenv.git --single-branch --branch master
	git clone https://github.com/int-brain-lab/ibllib.git --single-branch --branch develop ibllib-repo
	git clone https://github.com/int-brain-lab/iblapps.git --single-branch --branch develop
	git clone https://github.com/int-brain-lab/analysis.git --single-branch --branch master
	git clone https://github.com/int-brain-lab/IBL-pipeline.git --single-branch --branch master
	git clone https://github.com/cortex-lab/phylib --single-branch --branch master
	git clone https://github.com/cortex-lab/phy --single-branch --branch master

	micromamba activate
	conda-develop ./ibllib-repo
	conda-develop ./iblapps
	conda-develop ./analysis
	conda-develop ./IBL-pipeline
	conda-develop ./phylib
	conda-develop ./phy
EOF

# clean up -----------------------------------------------------------------------------
USER 0:999
RUN <<-EOF
	micromamba activate
	micromamba update -yqa
	micromamba clean -ya
	conda-env export --no-builds --ignore-channels >"${ROOT_ENV_PATH}/iblenv.locked.yml"
	rm -rf /tmp/*
EOF

ENTRYPOINT [ "/bin/bash", "-lc" ]
CMD [ "tail", "-f", "/dev/null" ]

## Stage 2 =============================================================================
## Final/Target IBL Env Image
## -------------------------------------------------------------------------------------
FROM scratch as iblenv
COPY --from=iblenv_build / /

ARG IMAGE_CREATED
ARG IMAGE_VERSION

ENV IBL_PATH_ROOT=${ROOT_ENV_PATH}
ENV TZ="Europe/Lisbon"
ENV LANG=en_US.utf8
ENV LC_ALL=en_US.utf8
ENV LANGUAGE=en_US.utf8
ENV LC_CTYPE=en_US.utf8
ENV QT_QPA_PLATFORM=offscreen
ENV ALYX_INSTANCE=local
ENV ALYX_SRC_PATH=/var/www/alyx-local
ENV ALYX_CACHE_DIR=/var/www/alyx-local/cache
ENV PYTHONPATH=/var/www/alyx-local/alyx
ENV ALYX_URL=alyx.internationalbrainlab.org
ENV ALYX_LOGIN=ibl_dev
ENV ALYX_PWD=
ENV CACHE_DIR=
ENV HTTP_DATA_SERVER=https://ibl.flatironinstitute.org
ENV HTTP_DATA_SERVER_LOGIN=
ENV HTTP_DATA_SERVER_PWD=
ENV DJANGO_SECRET_KEY=
ENV DJANGO_SETTINGS_MODULE=alyx.settings
ENV FLATIRON_SERVER=${HTTP_DATA_SERVER}
ENV FLATIRON_SERVER_LOGIN=${HTTP_DATA_SERVER_LOGIN}
ENV FLATIRON_SERVER_PWD=${HTTP_DATA_SERVER_PWD}

LABEL org.opencontainers.image.ref.name="iblenv"
LABEL org.opencontainers.image.authors "Joseph Burling"
LABEL org.opencontainers.image.vendor="International Brain Lab"
LABEL org.opencontainers.image.title "iblenv_debian_micromamba"
LABEL org.opencontainers.image.description "A unified environment for all IBL repositories."
LABEL org.opencontainers.image.created="$IMAGE_CREATED"
LABEL org.opencontainers.image.version="$IMAGE_VERSION"

WORKDIR ${IBL_PATH_ROOT}
USER 999:999
ENTRYPOINT [ "/bin/bash", "-lc" ]
CMD [ ]

# 0. Base Image: python:3.9-slim
# This image is the official image from Python, which has Python 3.9 installed
# Slim means that it only contains minimal packages.
FROM python:3.9-slim

ARG environment=prod
ENV ENVIRONMENT=${environment}

ARG extras= 

ENV BUILD_TIME_FILE=/app/build_time

# # 1. Create a (non-root) app- user account and set our working directory
# Using UID and GID 1000 as it corresponds to the primary user on popular Linux distros 
# This creates the directory and sets it as current,
# for both the docker build as well as when running.
RUN apt-get -y update && \
        groupadd -r -g 1000 app-group && \
        useradd -m -d /app -s /bin/bash -g 1000 -u 1000 app-user
ENV PATH="/app/.local/bin:${PATH}"
USER app-user'
WORKDIR /app

RUN apt update \
        && apt install -y \
        bash \
        netcat-openbsd

# # 2. Install pinned requirments.
# # This step could technically be skipped, but then in (step 3) our package would
# # install whatever latest versions of its dependencies, instead of the ones we trust.
# Copy over the requirements file with pinned production dependency versions
COPY requirements-${ENVIRONMENT}.txt .
# Install the pinned prioduction dependencies
RUN pip install --upgrade pip && \
        pip install --no-cache-dir --upgrade -r requirements-prod.txt && \
        mkdir -p /app/logs/

# # 3. Install our package and CLI program.
# Copy over the rest of the context (I.e. the repo root-dir, minus .dockerignore)
COPY --chown=app-user:app-group . .
# Install the packages
RUN pip install --no-cache-dir --upgrade .${extras} && \
        chmod +x entrypoint.sh && \
        echo $(date -u -Iseconds) > ${BUILD_TIME_FILE}

ENTRYPOINT ["/bin/bash", "/app/statup.sh", "my-app"]
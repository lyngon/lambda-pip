ARG py=3.9
FROM python:${py}-slim
ENV PYTHON_VERSION=py

ARG uid=1000
ARG gid=1000

ARG input_dir=/asset-input
ENV INPUT_DIR=${input_dir}

ARG output_dir=/asset-output
ENV OUTPUT_DIR=${output_dir}

ENV BUILD_TIME_FILE=/app/build_time

# Run as user, not root
RUN apt-get -y update && \
        apt-get -y install zip && \
        groupadd -r -g ${gid} app-group && \
        useradd -m -d /app -s /bin/bash -g ${gid} -u ${uid} app-user && \
        mkdir -p ${INPUT_DIR} && \
        mkdir -p ${OUTPUT_DIR}
USER app-user
WORKDIR /app

# Copy over the script, and make it executable
COPY --chown=app-user:app-group lambda_pip.sh /app/script/
ENV PATH="/app/script:${PATH}" 
RUN chmod +x /app/script/lambda_pip.sh && \
        echo $(date -u -Iseconds) > ${BUILD_TIME_FILE}

ENTRYPOINT ["lambda_pip.sh"]
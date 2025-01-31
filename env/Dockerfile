FROM python:3.13-slim as base

USER root

ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y \
    curl \
    tar \
    wget \
    git \
    build-essential \
    ca-certificates \
    sudo \
    procps \
    vim \
    less \
    && rm -rf /var/lib/apt/lists/*

# Install UV and add to PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Create virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies using UV
COPY /env/requirements.txt /tmp/
RUN uv pip install -r /tmp/requirements.txt

# Set up the workspace
ENV PYTHONPATH=/workspace/src
WORKDIR /workspace

COPY src /workspace/src

CMD gunicorn -k uvicorn.workers.UvicornWorker \
    -t $TIMEOUT \
    -w $UVI_WORKERS \
    --max-requests 1000 \
    --max-requests-jitter 50 \
    --bind "localhost:$PORT" \
    --preload \
    --graceful-timeout 600 \
    $FASTAPI_APP
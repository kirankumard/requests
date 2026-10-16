FROM mcr.microsoft.com/devcontainers/base:ubuntu

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN apt-get update && apt-get install -y python3 python3-pip --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV UV_LINK_MODE=copy
ENV PATH="/usr/local/bin:$PATH"
FROM python:3.12-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    UV_SYSTEM_PYTHON=1

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv>=0.6.15

# Copy project metadata first for better caching
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen || true

# Copy the rest
COPY . .

CMD ["python", "-c", "print('Hello, Zero2AI in Docker')"]


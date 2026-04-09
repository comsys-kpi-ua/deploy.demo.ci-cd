# deploy-demo-ci-cd

Demo project for CI/CD pipeline with Flask application.

## Description

Simple Flask web application with health check endpoint, demonstrating containerization with Docker and uv.

## Development

```bash
# Install with dev dependencies
uv sync --dev

# Run linter
uv run ruff check .

# Fix automatically
uv run ruff check --fix .

# Run tests
uv run pytest
```

## Quick Start

```bash
# Install dependencies
uv sync

# Run locally
python main.py
```

## Docker

```bash
# Build
docker build -t deploy-demo .

# Run
docker run -p 5000:5000 deploy-demo
```

## Endpoints

- `/` - Returns app version
- `/health` - Health check endpoint

## License

MIT - see [LICENSE](LICENSE)
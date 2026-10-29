# DevOps Capstone: Accounts Microservice

[![Build Status](https://github.com/Kalyani-Patil-06/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Kalyani-Patil-06/devops-capstone-project/actions/workflows/ci-build.yaml)

A Flask-based Accounts REST API for the DevOps Capstone project. This repository contains the microservice, automated tests, CI workflow, Docker configuration, and Kubernetes and Tekton deployment resources.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

The API listens on `http://127.0.0.1:8080`.

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/accounts` | Create an account |
| GET | `/accounts` | List accounts |
| GET | `/accounts/<id>` | Read an account |
| PUT | `/accounts/<id>` | Update an account |
| DELETE | `/accounts/<id>` | Delete an account |

Example:

```bash
curl -i -X POST http://127.0.0.1:8080/accounts -H 'Content-Type: application/json' -d '{"name":"Jane Doe","email":"jane@example.com"}'
curl -i http://127.0.0.1:8080/accounts
```

## Tests and quality checks

```bash
flake8 service tests
nosetests
```

Run these commands in your configured project environment. The GitHub Actions workflow should also run the required checks.

## Container

```bash
docker build -t accounts:local .
docker run --rm -p 8080:8080 accounts:local
```

## Project contents

- `service/` — Flask application and account service code
- `tests/` — automated tests
- `.github/workflows/` — GitHub Actions workflow
- `Dockerfile` — container image configuration
- `kubernetes/` — Kubernetes configuration
- `tekton/` — Tekton pipeline resources
- `user-story.md` — project user stories

## Note

The API currently uses in-memory storage, so account data resets when the process restarts. Kubernetes and Tekton configurations may require adjustments for your cluster and container registry.

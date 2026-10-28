# Accounts Microservice

Starter project for a Flask-based Accounts REST API and DevOps capstone activities.

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

## Container

```bash
docker build -t accounts:local .
docker run --rm -p 8080:8080 accounts:local
```

## Important submission note

This is a starter scaffold, not evidence that every lab task has been completed. Replace placeholders, run the actual lab activities, and capture genuine screenshots/output from your own GitHub, Kubernetes, and Tekton environment. The API uses in-memory storage and resets when the process restarts. Kubernetes and Tekton files are templates that may need adaptation to your cluster and registry.

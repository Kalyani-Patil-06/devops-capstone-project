# User Story — Accounts Microservice

**As a** service consumer, **I want** to create, view, update, and delete customer accounts through a REST API, **so that** account information can be managed consistently.

## Acceptance criteria

- A valid account can be created with a name and email address.
- Accounts can be listed and retrieved by ID.
- Existing account fields can be updated.
- An account can be deleted.
- Invalid requests return a useful 4xx response.
- The service exposes a health endpoint and automated tests.

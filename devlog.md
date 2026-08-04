# Layered Backend Architecture

Request Flow

Client
↓
API
↓
Dependencies
↓
Services
↓
Repositories
↓
Database

Why?

- Separation of concerns
- Easier testing
- Better maintainability
- Reusable business logic
- Cleaner codebase

Interview takeaway:
In a layered architecture, each layer has one responsibility and communicates only with adjacent layers.



## Layer Responsibilities

API
- Receives HTTP requests
- Returns HTTP responses
- Calls services

Service
- Contains business logic
- Coordinates application workflows
- Calls repositories

Repository
- Performs database operations
- Hides SQL/ORM details from services

Why separate them?
- Separation of concerns
- Reusability
- Easier testing
- Easier maintenance
- Centralized database access

Interview takeaway:
Routes should not contain business logic or database queries. Each layer should have a single, well-defined responsibility.


## Layer Responsibilities (Memory Trick)

API → Asks
- Handles HTTP requests/responses

Service → Decides
- Business rules
- Coordinates workflows

Repository → Fetches
- Database queries
- ORM/SQL

Database → Stores
- Persistent data

## July 27

### Completed
- Studied FastAPI request lifecycle in depth.
- Understood SQLAlchemy Session lifecycle.
- Learned how Depends(get_db) provides a request-scoped session.
- Learned why yield is used instead of return.
- Understood Session vs Transaction.
- Learned Dirty Checking and Identity Map.

### Key Takeaways
- One HTTP request gets one SQLAlchemy Session.
- Session tracks ORM objects and generates SQL during commit().
- Identity Map ensures one Python object per database row within a Session.

### Next
- Unit of Work
- flush() vs commit()
- rollback()

## Date: 2026-07-31

### Completed
- Investigated Alembic migration failure.
- Learned PostgreSQL authentication vs authorization.
- Explored PostgreSQL roles, database ownership, and schema ownership.
- Fixed database ownership mismatch.
- Successfully generated Alembic migration.

### Problems Faced
- `permission denied for schema public`
- PostgreSQL required password authentication (`scram-sha-256`) for local connections.
- Application user did not own the target database.

### Key Learnings
- Alembic stores migration history in the `alembic_version` table.
- Database ownership affects schema permissions.
- Authentication verifies identity; authorization controls allowed actions.
- Always investigate before granting permissions.
## Authentication Foundation

### Completed
- Created `app/core/` package.
- Added `security.py` for authentication utilities.
- Added `config.py` using Pydantic Settings.
- Configured `.env` for application secrets.
- Added `.env` to `.gitignore`.
- Installed:
  - passlib[bcrypt]
  - python-jose[cryptography]
  - pydantic-settings
  - python-dotenv

### Learned
- Difference between hashing and encryption.
- Why bcrypt is preferred for password storage.
- Role of salts in password hashing.
- JWT fundamentals (Header, Payload, Signature).
- Why configuration should be separated from business logic.
- Why environment variables are used in production.

### Next
- Implement JWT creation.
- Implement JWT verification.
- Build authentication service and login endpoint.

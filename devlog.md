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

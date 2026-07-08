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

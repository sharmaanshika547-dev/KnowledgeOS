# Layered Architecture

API
- Receives HTTP requests
- Returns HTTP responses
- Calls services

Service
- Contains business logic
- Independent of FastAPI
- Reusable by multiple clients

Repository
- Talks to the database
- Hides SQL/ORM details
- Returns data to services

Database
- Stores persistent data

Key Principles
- Separation of Concerns
- Single Responsibility Principle
- Framework Independence
- Reusability
- Abstraction

Memory Trick

API → Asks

Service → Decides

Repository → Fetches

Database → Stores

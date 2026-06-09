# Architecture

## Current Architecture

Phase 1 uses a simple monolithic architecture.

Client
↓
FastAPI
↓
Python List (notes_db)

---

## Why This Architecture?

The purpose of Phase 1 is to understand:

* HTTP
* FastAPI Routing
* Request Validation
* Response Models
* CRUD Operations

without introducing database complexity.

---

## Request Lifecycle

### Create Note

Client
↓
POST /notes
↓
FastAPI Route
↓
Pydantic Validation
↓
notes_db
↓
JSON Response

---

### Read Notes

Client
↓
GET /notes
↓
FastAPI Route
↓
notes_db
↓
JSON Response

---

### Update Note

Client
↓
PUT /notes/{id}
↓
Find Note
↓
Modify Data
↓
JSON Response

---

### Delete Note

Client
↓
DELETE /notes/{id}
↓
Remove Note
↓
204 No Content

---

## Components

### main.py

Application entry point.

Responsibilities:

* Create FastAPI application
* Register routers
* Configure metadata

---

### note_routes.py

Notes API.

Responsibilities:

* Create notes
* Read notes
* Update notes
* Delete notes

---

### note.py

Pydantic schemas.

Responsibilities:

* Request validation
* Response serialization
* API documentation

---

## Current Bottlenecks

### Storage

Current storage:

Python List

Problems:

* Data disappears on restart
* Cannot scale
* Cannot query efficiently

---

## Planned Phase 2 Architecture

Client
↓
FastAPI
↓
Repository Layer
↓
PostgreSQL

Benefits:

* Persistent storage
* Better querying
* Real database relationships

---

# KnowledgeOS

KnowledgeOS is a personal knowledge management backend built with FastAPI.

The goal of this project is not only to build a backend application, but also to progressively learn backend engineering, databases, authentication, cloud infrastructure, distributed systems, and AI-powered features.

Current Version: Phase 1 (In-Memory CRUD)

---

## Features

### Notes Management

* Create Notes
* Read Notes
* Update Notes
* Delete Notes

### Validation

* Request validation using Pydantic
* Structured response models

### API Documentation

* Interactive Swagger UI
* Automatic OpenAPI schema generation

---

## Tech Stack

* Python 3.11+
* FastAPI
* Pydantic

---

## Project Structure

knowledge-os/

app/
├── main.py
├── api/
│   └── note_routes.py
├── schemas/
│   └── note.py

README.md
architecture.md
roadmap.md
devlog.md
requirements.txt

---

## Getting Started

### Clone Repository

git clone <repository-url>

cd knowledge-os

### Create Virtual Environment

python -m venv venv

### Activate Environment

Linux / macOS:

source venv/bin/activate

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Server

uvicorn app.main:app --reload

---

## API Documentation

Swagger UI:

http://localhost:8000/docs

ReDoc:

http://localhost:8000/redoc

---

## Current Limitations

This is an educational Phase 1 implementation.

Current limitations:

* In-memory storage only
* Data resets after restart
* No authentication
* No PostgreSQL database
* No user accounts

---

## Learning Goals

This project is being built to learn:

* Backend Development
* API Design
* Database Design
* Authentication
* System Design
* Cloud Infrastructure
* AI Systems

---

## Future Roadmap

* PostgreSQL Integration
* Authentication (JWT)
* Workspaces
* Folders
* File Uploads
* AI Summaries
* Semantic Search
* RAG Pipelines
* Cloud Deployment

---

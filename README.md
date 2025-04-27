# 🦋 Butterflygarden - API

A project developed in **FastAPI** to **Butterflygardens** containing different species of butterflies **Butterflies**.

Each garden can host **multiple butterfly species**, allowing for organized and detailed management of butterfly data.

## 🚀 Technologies Used
- **Python 3.11**
- **FastAPI** (High-performance web framework for APIs)
- **SQLAlchemy** (ORM for relational database management)
- **MySQL** (Relational Database)
- **Docker** and **Docker Compose** (for containerization and deployment)
- **Uvicorn** (ASGI server for FastAPI applications)
- **Virtual Environment** (for dependency management and project isolation)

## 📚 Project Description

The system's main objectives are:
- Manage multiple butterfly gardens.
- Assign multiple butterfly species to each garden.
- Facilitate querying butterflies by their corresponding garden.
- Perform CRUD operations (Create, Read, Update, Delete) for both gardens and butterflies.

Each **Butterflygarden** includes:
- Name
- Location

Each **Butterfly** includes:
- Name
- Species (butterfly type)
- Color
- Direct association to a specific garden

### ✨ Main Features:
- Create and manage butterfly gardens.
- Register butterflies to specific gardens.
- List all gardens and their associated butterflies.
- Edit and delete both gardens and butterflies.

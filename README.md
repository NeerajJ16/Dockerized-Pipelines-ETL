# 🐳 Dockerized ETL Pipeline with Railway PostgreSQL

This project demonstrates a simple, containerized ETL (Extract, Transform, Load) pipeline using Python and Docker. The ETL script fetches user data from a public API and loads it into a PostgreSQL database hosted on [Railway](https://railway.app/).

## 🚀 What This Project Does

✅ Pulls user data from a public API  
✅ Connects to a PostgreSQL database hosted on Railway  
✅ Inserts user data into a table (`users`)  
✅ Runs entirely inside Docker — no Python or database setup required locally

---
## 🛠️ Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running
- A PostgreSQL database (e.g., from [Railway](https://railway.app))
---

## 📄 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/yourusername/docker-etl-project.git
cd docker-etl-project
```
### 2. Create .env file
```
cp .env.example .env
```
This creates .env file in root folder and edit with all details fetched from Railway Postgres public domain. (postgresql://user:password@hostname:port/databasename)

---

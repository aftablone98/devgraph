# 🚀 DevGraph

DevGraph is a graph-powered developer profile application built using **Python, FastAPI, and CognoDB**.

The application stores developers, their skills, and projects as connected graph data and exposes the information through a REST API and a web frontend.

---

## 📌 Features

- Developer profile management
- Skills stored as graph relationships
- Projects stored as graph relationships
- FastAPI REST API
- CognoDB graph database
- Cypher queries
- Python Neo4j-compatible driver
- Interactive API documentation with Swagger
- Web frontend
- Developer graph visualization
- Environment variables for database credentials
- Git-safe configuration using `.gitignore`

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      Browser        │
                    │    Frontend :3000   │
                    └──────────┬──────────┘
                               │
                               │ HTTP / REST
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │      API :8002      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Python Models     │
                    │    Cypher Queries   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      CognoDB        │
                    │    Graph Database   │
                    └─────────────────────┘


🛠️ Tech Stack
Backend
Python
FastAPI
Uvicorn
Pydantic
python-dotenv
Neo4j Python Driver
Database
CognoDB
Cypher
Frontend
HTML
CSS
JavaScript
D3.js
Development
Linux / Ubuntu WSL
Git
GitHub
Python Virtual Environment


🗂️ Project Structure

devgraph/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   ├── test_cognodb.py
│   ├── test_db.py
│   ├── test_models.py
│   └── test_profile.py
│
├── frontend/
│   └── index.html
│
├── data/
│
├── queries/
│
├── scripts/
│
├── .gitignore
├── README.md
└── .venv/


🔐 Environment Variables

Create:

backend/.env

Example:

COGNODB_URI=bolt+s://your-instance.databases.cognodb.com
COGNODB_USERNAME=cognodb
COGNODB_PASSWORD=your-password

Never commit .env to Git.

The .gitignore file excludes environment variables and Python-generated files.


⚙️ Setup

Clone the repository:

git clone <your-repository-url>
cd devgraph

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install dependencies:

pip install neo4j python-dotenv fastapi uvicorn

Configure:

backend/.env

with your CognoDB credentials.



🌱 Seed the Database

Run:
python3 scripts/seed.py

This seeds CognoDB with sample developer, skill, and project data.

The seed script is idempotent, so it can safely be run multiple times without creating duplicate relationships.




🗄️ Test CognoDB Connection

Run:

python3 backend/test_cognodb.py

Expected result:

Successfully connected to CognoDB!
🧪 Test Database Models

Run:

python3 backend/test_models.py

The application should show developer skills and projects.

Example:

Aftab Lone → KNOWS → Docker
Aftab Lone → KNOWS → Kubernetes
Aftab Lone → KNOWS → Python

Aftab Lone → WORKED_ON → Linux Automation
Aftab Lone → WORKED_ON → Docker DevOps
⚡ Start the Backend

From the project root:

uvicorn backend.app:app --reload --host 0.0.0.0 --port 8002

Backend:

http://localhost:8002
📚 API Documentation

FastAPI automatically provides Swagger documentation.

Open:

http://localhost:8002/docs
🔌 API Endpoints
Method	Endpoint	Description
GET	/	API status
GET	/health	Database health check
GET	/users/{user_name}	Get complete profile
GET	/users/{user_name}/skills	Get user skills
POST	/users	Create user
POST	/users/{user_name}/skills	Add skill
POST	/users/{user_name}/projects	Add project
👤 Example User

Example profile:

Name: Aftab Lone
Role: DevOps Engineer

Skills:

Python
Docker
Kubernetes

Projects:

Linux Automation
Docker DevOps
🕸️ Graph Model

DevGraph represents developer information as connected graph data.

                 Python
                    ▲
                    │
                  KNOWS
                    │
Docker ◄────── Aftab Lone ──────► Kubernetes
                    │
                WORKED_ON
                    │
                    ▼
             Linux Automation
                    │
                    ▼
              Docker DevOps
Graph relationships
(:User)-[:KNOWS]->(:Skill)

(:User)-[:WORKED_ON]->(:Project)
🌐 Start the Frontend

From the frontend directory:

cd frontend

Start the development server:

python3 -m http.server 3000

Open:

http://localhost:3000

The frontend communicates with the FastAPI backend:

Frontend :3000
       ↓
FastAPI :8002
       ↓
CognoDB
🔎 Example API Request

Get a developer profile:

curl "http://localhost:8002/users/Aftab%20Lone"

Example response:

{
  "name": "Aftab Lone",
  "role": "DevOps Engineer",
  "skills": [
    "Docker",
    "Kubernetes",
    "Python"
  ],
  "projects": [
    "Linux Automation",
    "Docker DevOps"
  ]
}
❤️ Health Check

Run:

curl http://localhost:8002/health

Expected:

{
  "status": "healthy",
  "database": "CognoDB"
}
🔒 Security

Sensitive configuration is stored outside Git.

Ignored files include:

.env
*.env
.venv/
__pycache__/
*.pyc

Database passwords should never be committed to the repository.

🚀 Future Improvements
Authentication and authorization
Developer search
More graph relationship types
Advanced graph visualization
Docker deployment
CI/CD pipeline
Automated testing
Cloud deployment
Monitoring and observability
Production deployment
👨‍💻 Author

Aftab Lone

📄 License

This project is created for learning, portfolio, and technical demonstration purposes.

Save:

```text
Ctrl+O
Enter
Ctrl+X

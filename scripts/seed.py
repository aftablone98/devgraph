import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.db import db


USERS = [
    {
        "name": "Aftab Lone",
        "role": "DevOps Engineer",
        "skills": [
            "Python",
            "Docker",
            "Kubernetes"
        ],
        "projects": [
            {
                "name": "Linux Automation",
                "description": "Linux automation and system administration scripts",
                "required_skills": [
                    "Python",
                    "Linux"
                ]
            },
            {
                "name": "Docker DevOps",
                "description": "Containerized DevOps application using Docker",
                "required_skills": [
                    "Docker",
                    "Python"
                ]
            }
        ]
    },
    {
        "name": "Sarah",
        "role": "Software Engineer",
        "skills": [
            "Python",
            "Docker",
            "Kubernetes"
        ],
        "projects": [
            {
                "name": "Cloud DevOps Platform",
                "description": "Cloud-native application deployment platform",
                "required_skills": [
                    "Docker",
                    "Kubernetes",
                    "Python"
                ]
            }
        ]
    }
]


def seed_database():
    with db.driver.session() as session:

        for user in USERS:

            # Create or update user
            session.run(
                """
                MERGE (u:User {name: $name})
                SET u.role = $role
                """,
                name=user["name"],
                role=user["role"]
            )

            # Add skills and KNOWS relationships
            for skill in user["skills"]:
                session.run(
                    """
                    MATCH (u:User {name: $user_name})

                    MERGE (s:Skill {name: $skill})

                    MERGE (u)-[:KNOWS]->(s)
                    """,
                    user_name=user["name"],
                    skill=skill
                )

            # Add projects and WORKED_ON relationships
            for project in user["projects"]:
                session.run(
                    """
                    MATCH (u:User {name: $user_name})

                    MERGE (p:Project {name: $project_name})
                    SET p.description = $description

                    MERGE (u)-[:WORKED_ON]->(p)
                    """,
                    user_name=user["name"],
                    project_name=project["name"],
                    description=project["description"]
                )

                # Add project skill requirements
                for skill in project["required_skills"]:
                    session.run(
                        """
                        MERGE (s:Skill {name: $skill})

                        MATCH (p:Project {name: $project_name})

                        MERGE (p)-[:REQUIRES]->(s)
                        """,
                        skill=skill,
                        project_name=project["name"]
                    )

            print(f"✅ Seeded: {user['name']}")


if __name__ == "__main__":

    try:
        db.verify_connection()

        print("✅ Connected to CognoDB")
        print("🌱 Starting database seed...\n")

        seed_database()

        print("\n✅ Database seeding completed successfully!")

    except Exception as e:
        print(f"❌ Database seed failed: {e}")
        raise

    finally:
        db.close()

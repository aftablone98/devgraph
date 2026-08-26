import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


# Load environment variables
load_dotenv("backend/.env")

URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")


# Create database driver
driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


try:
    # Test connection
    driver.verify_connectivity()
    print("✅ Successfully connected to CognoDB!")

    with driver.session() as session:

        # Remove duplicate test users
        session.run("""
            MATCH (u:User)
            WITH u.name AS name, collect(u) AS users
            FOREACH (duplicate IN tail(users) | DELETE duplicate)
        """)

        # Create the user only if it doesn't already exist
        session.run("""
            MERGE (u:User {name: "Aftab Lone"})
            SET u.role = "DevOps Engineer"
        """)

        print("✅ User created/updated!")

        # Read the user
        result = session.run("""
            MATCH (u:User {name: "Aftab Lone"})
            RETURN u.name AS name, u.role AS role
        """)

        print("\n📌 User in CognoDB:")

        for record in result:
            print(
                f"Name: {record['name']} | "
                f"Role: {record['role']}"
            )

finally:
    driver.close()

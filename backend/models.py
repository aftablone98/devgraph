from backend.db import db


def create_user(name, role):
    with db.driver.session() as session:
        result = session.run(
            """
            MERGE (u:User {name: $name})
            SET u.role = $role
            RETURN u.name AS name, u.role AS role
            """,
            name=name,
            role=role
        )

        return result.single()


def add_skill(user_name, skill_name):
    with db.driver.session() as session:
        result = session.run(
            """
            MATCH (u:User {name: $user_name})

            MERGE (s:Skill {name: $skill_name})

            MERGE (u)-[:KNOWS]->(s)

            RETURN u.name AS user, s.name AS skill
            """,
            user_name=user_name,
            skill_name=skill_name
        )

        return result.single()


def get_user_skills(user_name):
    with db.driver.session() as session:
        result = session.run(
            """
            MATCH (u:User {name: $user_name})-[:KNOWS]->(s:Skill)
            RETURN u.name AS user, s.name AS skill
            ORDER BY s.name
            """,
            user_name=user_name
        )

        return list(result)


def add_project(user_name, project_name, description):
    with db.driver.session() as session:
        result = session.run(
            """
            MATCH (u:User {name: $user_name})

            MERGE (p:Project {name: $project_name})
            SET p.description = $description

            MERGE (u)-[:WORKED_ON]->(p)

            RETURN
                u.name AS user,
                p.name AS project,
                p.description AS description
            """,
            user_name=user_name,
            project_name=project_name,
            description=description
        )

        return result.single()



def get_user_profile(user_name):
    with db.driver.session() as session:
        result = session.run(
            """
            MATCH (u:User {name: $user_name})

            OPTIONAL MATCH (u)-[:KNOWS]->(s:Skill)

            OPTIONAL MATCH (u)-[:WORKED_ON]->(p:Project)

            RETURN
                u.name AS name,
                u.role AS role,
                collect(DISTINCT s.name) AS skills,
                collect(DISTINCT p.name) AS projects
            """,
            user_name=user_name
        )

        return result.single()


def get_user_skills(user_name):
    with db.driver.session() as session:
        result = session.run(
            """
            MATCH (u:User {name: $user_name})-[:KNOWS]->(s:Skill)
            RETURN s.name AS skill
            ORDER BY s.name
            """,
            user_name=user_name
        )

        return [record["skill"] for record in result]

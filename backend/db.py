import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv("backend/.env")


URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")


class Database:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            URI,
            auth=(USERNAME, PASSWORD)
        )

    def verify_connection(self):
        self.driver.verify_connectivity()
        return True

    def close(self):
        self.driver.close()


db = Database()

from db import db


try:
    db.verify_connection()
    print("✅ Database module connected to CognoDB!")

finally:
    db.close()

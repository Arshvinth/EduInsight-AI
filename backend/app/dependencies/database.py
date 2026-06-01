from app.core.database import SessionLocal


# Dependency that provides a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
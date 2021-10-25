# Alembic guide:
https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396  
Run:  
```alembic revision --autogenerate -m "First migration"```  
- Generates a migration file  
```alembic upgrade head```  
- Modifies the tables based on migration files

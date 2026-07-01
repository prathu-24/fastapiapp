from sqlalchemy import create_engine, inspect, text

engine = create_engine('postgresql://postgres:admin123@localhost:5432/student_db')
inspector = inspect(engine)
print('tables public =', inspector.get_table_names(schema='public'))
print('schemas =', inspector.get_schema_names())
with engine.connect() as conn:
    result = conn.execute(text("SELECT table_schema, table_name FROM information_schema.tables WHERE table_name='users';"))
    print('users rows =', result.fetchall())
    result = conn.execute(text('SELECT version_num FROM alembic_version;'))
    print('alembic_version =', result.fetchall())

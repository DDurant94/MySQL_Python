from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
  try:
    cursor = conn.cursor()
    query = """ALTER TABLE Trainers
    
    """
    cursor.execute(query)
    conn.commit()
  except Exception as e:
    print(f"Error: {e}")
  finally:
    cursor.close()
    conn.close()
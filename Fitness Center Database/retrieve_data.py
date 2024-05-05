from connect_mysql import connect_database

def view_menu(cursor):
  while True:
    view_choice = input("Type Trainers, Members, Sessions to view or Exit: ").lower()
    if view_choice == "members":
      print("Members:")
      view_members(cursor)
    elif view_choice == "trainers":
      print("Invalid Choice")
      view_trainers(cursor)
    elif view_choice == "sessions":
      print("Workout Sessions:")
      view_workout_sessions(cursor)
    elif view_choice == "exit":
      break
    else:
      print("Invalid Choice")

def view_members(cursor):
  query = "SELECT * FROM Members"
  cursor.execute(query)
  for row in cursor.fetchall():
    print(row)

def view_trainers(cursor):
  query = "SELECT * FROM trainers"
  cursor.execute(query)
  for row in cursor.fetchall():
    print(row)

def view_workout_sessions(cursor):
  query = "SELECT * FROM Workoutsessions"
  cursor.execute(query)
  for row in cursor.fetchall():
    print(row)

def view_member(member_name,cursor):
  query = """SELECT m.id,m.name, m.age,t.name
  FROM members as m
  JOIN trainers as t
  ON t.id = m.id
  WHERE m.name = %s
  """
  cursor.execute(query,(member_name,))
  info = cursor.fetchall()
  print(info)
  if info:
    print(f"{info[0][1]}:\nI.D. Number: {info[0][0]}\nAge: {info[0][2]}\nTrainer: {info[0][3]}")
  else:
    print(f"{member_name} not found")

def view_trainer(trainer_name,cursor):
  query = """SELECT t.name,t.email, t.id, m.name
  FROM trainers as t
  JOIN members as m
  ON m.id = t.id
  WHERE t.name = %s
  """
  cursor.execute(query,(trainer_name,))
  info = cursor.fetchall()
  if info:
    query_clients ="""SELECT m.name
    FROM members as m
    JOIN trainers as t
    ON m.id = t.id
    GROUP BY t.id"""
    cursor.execute(query_clients)
    members = cursor.fetchall()
    print(f"{info[0][0]}:\nI.D. Number: {info[0][2]}\nEmail: {info[0][1]}\nClients: {members}")
  else:
    print(f"{trainer_name} not found")

def view_session(session_id):
  query = "SELECT * FROM Members"

def main_retrieve():
  conn = connect_database()
  if conn is not None:
    try:
      cursor = conn.cursor()
      while True:
        print("Viewing Menu:\n1. View All\n2. View Member\n3. View Trainer\n4. View Session\n5. Exit")
        menu_choice = input("Choose Menu Option: ")
        if menu_choice == "1":
          view_menu(cursor)
        elif menu_choice == "2":
          member_name = input("Enter members Full Name: ").title()
          view_member(member_name,cursor)
        elif menu_choice == "3":
          trainer_name = input("Enter Trainers Full Name: ").title()
          view_trainer(trainer_name,cursor)
        elif menu_choice == "4":
          view_session(cursor)
        elif menu_choice == "5":
          break
        else:
          print("Invalid Choice")
    except Exception as e:
      print(f"Error: {e}")
    finally:
      cursor.close()
      conn.close()


def list_distinct_trainers():
  pass
  query = """SELECT DISTINCT t.id
  FROM members as m
  JOIN trainers as t 
  ON m.trainer_id = t.id"""
# A list of unique trainer IDs from the Members table

def count_members_per_trainer():
  pass
  query = """SELECT COUNT(m.trainer_id), t.name
  FROM members as m
  JOIN trainers as t
  ON m.trainer_id = t.id
  GROUP BY m.trainer_id"""
# A count of members grouped by their trainer IDs.

def get_members_in_age_range(start_age, end_age):
  pass
  query = """SELECT m.name, m.age m.trainer_id, t.name
  FROM members as m
  JOIN trainers as t
  ON m.trainer_id = t.id
  WHERE age BETWEEN 25 and 30"""
# checking ages between 25-30 list our name, age trainer_id
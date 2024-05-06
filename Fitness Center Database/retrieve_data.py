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
  ON m.trainer_id = t.id
  WHERE m.name = %s
  """
  cursor.execute(query,(member_name,))
  info = cursor.fetchall()
  if info:
    print(f"{info[0][1]}:\nI.D. Number: {info[0][0]}\nAge: {info[0][2]}\nTrainer: {info[0][3]}")
  else:
    print(f"{member_name} not found")

def view_trainer(trainer_name,cursor):
  query = """SELECT t.name,t.email, t.id, m.name
  FROM trainers as t
  JOIN members as m
  ON m.trainer_id = t.id
  WHERE t.name = %s
  """
  cursor.execute(query,(trainer_name,))
  info = cursor.fetchall()
  if info:
    print(f"{info[0][0]}:\nI.D. Number: {info[0][2]}\nEmail: {info[0][1]}\nClients:")
    for count,client in enumerate(info):
      print(f"{count +1}. {client[3]}")
  else:
    print(f"{trainer_name} not found")

def view_session(member_id,cursor):
  query = '''SELECT ws.id,ws.customer_id,ws.Duration_minutes, ws.Calories_burned, ws.date 
  FROM Workoutsessions as ws
  WHERE ws.customer_id = %s'''
  cursor.execute(query,(member_id,))
  info = cursor.fetchone()
  if info:
    print(info)
    print(f"Session I.D. Number: {info[0]}\n Customer I.D. Number: {info[1]}\n Duration: {info[2]} Minutes\nCalories Burned: {info[3]}\nDate: {info[4]}")
  else:
    print(f"Workout session with an Member I.D. Number {member_id} is not in Database")
    

def list_distinct_trainers(cursor):
  query = """SELECT DISTINCT t.name
  FROM members as m
  JOIN trainers as t 
  ON m.trainer_id = t.id"""
  cursor.execute(query)
  print("Trainers with Clients:")
  for row in cursor.fetchall():
    print(row[0])

def count_members_per_trainer(cursor):
  query = """SELECT COUNT(m.trainer_id), t.name
  FROM members as m
  JOIN trainers as t
  ON m.trainer_id = t.id
  GROUP BY m.trainer_id"""
  cursor.execute(query)
  for row in cursor.fetchall():
    print(f"Trainer: {row[1]}\nNumber of Clients: {row[0]}")

def get_members_in_age_range(start_age, end_age,cursor):
  query = """SELECT m.name, m.age, m.trainer_id, t.name, m.id
  FROM members as m
  JOIN trainers as t
  ON m.trainer_id = t.id
  WHERE m.age BETWEEN %s AND %s"""
  cursor.execute(query,(start_age,end_age))
  print(f"Members with an age between {start_age} and {end_age}:\n")
  for row in cursor.fetchall():
    print(f"Name: {row[0]} I.D. Number {row[4]}\nAge: {row[1]}\nTrainer: {row[3]} Trainer I.D. Number {row[2]}\n")

def main_retrieve():
  conn = connect_database()
  if conn is not None:
    try:
      cursor = conn.cursor()
      while True:
        print("Viewing Menu:\n1. View All\n2. View Member\n3. View Trainer\n4. View Session\n5. Members Between Ages\n6. Trainers With Clients\n7. Amount of Members Per Trainer\n8. Exit")
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
          member_id = int(input("Enter Member I.D. Number: "))
          view_session(member_id,cursor)
        elif menu_choice == "5":
          start_age = int(input("Enter Youngest Age: "))
          end_age = int(input("Enter Oldest Age: "))
          get_members_in_age_range(start_age, end_age,cursor)
        elif menu_choice == "6":
          list_distinct_trainers(cursor)
        elif menu_choice == "7":
          count_members_per_trainer(cursor)
        elif menu_choice == "8":
          break
        else:
          print("Invalid Choice")
    except Exception as e:
      print(f"Error: {e}")
    finally:
      cursor.close()
      conn.close()




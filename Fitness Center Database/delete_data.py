from connect_mysql import connect_database

def delete_members(member_id,cursor):
  check_query = "SELECT id FROM members WHERE id = %s"
  cursor.execute(check_query,(member_id,))
  member = cursor.fetchone() 
  if member:
    query = """DELETE FROM Members
    WHERE id = %s"""
    cursor.execute(query,(member_id,))
    print(f"Member with an I.D. Number of {member_id} was successfully deleted")
  else:
    print(f"No Member With I.D. Number {member_id}")

def delete_trainers(trainer_id,cursor):
  check_query = "SELECT id FROM trainers WHERE id = %s"
  cursor.execute(check_query,(trainer_id,))
  trainer = cursor.fetchone()
  if trainer:
    query = """DELETE FROM Trainers
    WHERE id = %s"""
    cursor.execute(query,(trainer_id,))
    print(f"Trainer with an I.D. Number of {trainer_id} was successfully deleted")
  else:
    print(f"No Trainer With I.D. Number {trainer_id}")

def delete_workout_sessions(session_id,cursor):
  check_query = "SELECT id FROM workoutsessions WHERE id = %s"
  cursor.execute(check_query,(session_id,))
  session = cursor.fetchone()
  if session:
    query = """DELETE FROM workoutsessions
    WHERE id = %s"""
    cursor.execute(query,(session_id,))
    print(f"Training Session with an I.D. Number of {session_id} was successfully deleted")
  else:
    print(f"No Workout Session With I.D. {session_id}")


def main_delete():
  conn = connect_database()
  if conn is not None:
    try:
      cursor = conn.cursor()
      while True:
        print("Delete Menu:\n1. Delete Member\n2. Delete Trainer\n3. Delete Session\n4. Exit")
        menu_choice = input("Choose Menu Option: ")
        if menu_choice == "1":
          member_id = int(input("Enter Members I.D. Number: "))
          delete_members(member_id,cursor)
        elif menu_choice == "2":
          trainers_id = int(input("Enter Trainer I.D. Number: "))
          delete_trainers(trainers_id,cursor)
        elif menu_choice == "3":
          session_id = int(input("Enter Session I.D. Number:"))
          delete_workout_sessions(session_id,cursor)
        elif menu_choice == "4":
          conn.commit()
          print("Database was successfully updated!")
          break
        else:
          print("Invalid Choice")
    except Exception as e:
      print(f"Error: {e}")
    finally:
      cursor.close()
      conn.close()

from connect_mysql import connect_database

def update_member(customer_id,cursor):
  search = '''SELECT id FROM Members WHERE id = %s'''
  cursor.execute(search,(customer_id,))
  info = cursor.fetchone()
  if info:
    new_name = input("Enter in members new first and last name: ").title()
    new_age = int(input("Enter in new members age: "))
    new_trainer_id = int(input("Enter in new trainer I.D. Number: "))
    query = "UPDATE Members SET name = %s, age = %s, trainer_id = %s WHERE id = %s"
    cursor.execute(query,(new_name,new_age,new_trainer_id,customer_id))
  else:
    print(f"Not Member in Database with I.D. Number {customer_id}")

def update_trainer(trainer_id,cursor):
  search = "SELECT id FROM Trainers WHERE id = %s"
  cursor.execute(search,(trainer_id,))
  info = cursor.fetchone()
  if info:
    new_trainer_name = input("Enter trainers new name: ").title()
    new_trainer_email = input("Enter trainers new email: ")
    query = "UPDATE Trainers SET name = %s, email = %s WHERE id = %s"
    cursor.execute(query,(new_trainer_name,new_trainer_email,trainer_id))
  else:
    print(f"Trainer with I.D. Number {trainer_id} is not in Database")

def update_workout_sessions(workout_id,customer_id,cursor):
  search = '''SELECT id FROM workoutsessions WHERE id = %s'''
  cursor.execute(search,(workout_id,))
  info = cursor.fetchone()
  if info:
    new_duration = int(input("Enter new Duration in minutes: "))
    new_cals_burned = new_duration * 3.5
    new_date = input("Enter new Date [YYYY-MM-DD]: ")
    query = "UPDATE workoutsessions SET Duration_minutes = %s, Calories_burned = %s, date = %s WHERE customer_id = %s and id = %s"
    cursor.execute(query,(new_duration,new_cals_burned,new_date,customer_id,workout_id))
  else:
    print(f"No Work out session with an I.D. Number {workout_id} or a Member I.D. Number {customer_id}")
  
def update_member_age(member_id,cursor):
  search = """SELECT id 
  FROM Members
  WHERE id = %s"""
  cursor.execute(search,(member_id,))
  info = cursor.fetchone()
  if info:
    new_age = int(input("Enter Members New Age: "))
    query = """UPDATE Members SET age = %s WHERE id = %s"""
    cursor.execute(query,(new_age,member_id))
  else:
    print("Member not found")

def main_update():
  conn = connect_database()
  if conn is not None:
    try:
      cursor = conn.cursor()
      while True:
        print("Edit Menu:\n1. Update Member\n2. Update Trainer\n3. Update Session\n4. Update Members Age\n5. Exit")
        menu_choice = input("Choose a menu option: ")
        if menu_choice == "1":
          member_id = int(input("Enter member I.D. Number: "))
          update_member(member_id,cursor)
        elif menu_choice == "2":
          trainer_id = int(input("Enter in Trainers I.D.: "))
          update_trainer(trainer_id,cursor)
        elif menu_choice == "3":
          member_id = int(input("Enter members I.d. Number: "))
          workout_id = int(input("Enter Workout Session I.D. Number: "))
          update_workout_sessions(workout_id,member_id,cursor)
        elif menu_choice =="4":
          member_id = int(input("Enter member I.D. Number: "))
          update_member_age(member_id,cursor)
        elif menu_choice == "5":
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

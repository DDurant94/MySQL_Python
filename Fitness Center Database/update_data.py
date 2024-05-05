from connect_mysql import connect_database

def update_member(name,age,trainer_id,customer_id,cursor):
  query = "UPDATE Members SET name = %s, age = %s, trainer_id = %s WHERE id = %s"
  cursor.execute(query,(name,age,trainer_id,customer_id))

def update_trainer(name,email,trainer_id,cursor):
  query = "UPDATE Trainers SET name = %s, email = %s WHERE id = %s"
  cursor.execute(query,(name,email,trainer_id))

def update_workout_sessions(duration,cals_burned,date,customer_id,workout_id,cursor):
  query = "UPDATE workoutsessions SET Duration = %s, Calories_burned = %s, date = %s WHERE customer_id = %s and id = %s"
  cursor.execute(query,(duration,cals_burned,date,customer_id,workout_id))
  


def main_update():
  conn = connect_database()
  if conn is not None:
    try:
      cursor = conn.cursor()
      while True:
        print("Edit Menu:\n1. Update Member\n2. Update Trainer\n3. Update Session\n4. Exit")
        menu_choice = input("Choose a menu option: ")
        if menu_choice == "1":
          member_id = int(input("Enter member I.D. Number: "))
          new_name = input("Enter in members first and last name: ")
          new_age = int(input("Enter in members age: "))
          new_trainer_id = int(input("Enter in trainers I.D. Number: "))
          update_member(new_name,new_age,new_trainer_id,member_id,cursor)
        elif menu_choice == "2":
          trainer_id = int(input("Enter in Trainers I.D.: "))
          new_trainer_name = input("Enter trainers new name: ")
          new_trainer_email = input("Enter trainers new email: ")
          update_trainer(new_trainer_name,new_trainer_email,trainer_id,cursor)
        elif menu_choice == "3":
          member_id = int(input("Enter members I.d. Number: "))
          workout_id = int(input("Enter Workout Session I.D. Number: "))
          new_duration = int(input("Enter new Duration in minutes: "))
          new_cals_burned = new_duration * 3.5
          new_date = input("Enter new Date [YYYY-MM-DD]: ")
          update_workout_sessions(new_duration,new_cals_burned,new_date,member_id,workout_id,cursor)
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


def update_member_age(member_id, new_age):
  pass
  query = """UPDATE Members SET age = %s WHERE id = %s"""
# update just age
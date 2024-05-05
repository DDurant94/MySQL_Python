from connect_mysql import connect_database

def add_member(name,age,trainer_id,cursor):
  search = "SELECT name FROM Members WHERE name = %s"
  cursor.execute(search,(name,))
  finding = cursor.fetchall()
  if finding:
    print(f"{name} is already in database")
  else:
    query = "INSERT INTO Members (name,age,trainer_id) VALUES (%s,%s,%s)"
    cursor.execute(query,(name,age,trainer_id))

def add_trainer(name,email,cursor):
  search = "SELECT name FROM trainers WHERE name = %s"
  cursor.execute(search,(name,))
  finding = cursor.fetchall()
  if finding:
    print(f"{name} is already in database")
  else:
    query = "INSERT INTO Trainers (name,email) VALUES (%s,%s)"
    cursor.execute(query,(name,email))

# fix the foreign key as well in this 
# add_workout_session(member_id, date, duration_minutes, calories_burned)
def add_workout_sessions(customer_id,duration_time,cals_burned,date,cursor):
  search = "SELECT id FROM workoutsessions as w WHERE customer_id = %s and date = %s"
  cursor.execute(search,(customer_id,date))
  finding = cursor.fetchall()
  if finding: # change date set up and tables
    print("Customer is already booked for that day.")
  else:
    query = "INSERT INTO workoutsessions (customer_id,duration_time,calories_burned,date) VALUES (%s,%s,%s,%s)"
    cursor.execute(query,(customer_id,duration_time,cals_burned,date))

def main_add():
  conn = connect_database()
  if conn is not None:
    try:
      cursor = conn.cursor()
      while True:
        print("Adding Information Menu:\n1. Add Member\n2. Add Trainer\n3. Add Session\n4. Exit")
        menu_choice = input("Choose menu option: ")
        if menu_choice == "1":
          name = input("Enter in members first and last name: ").title()
          age = int(input("Enter in members age: "))
          trainer_id = int(input("Enter in trainers I.D. Number: "))
          add_member(name,age,trainer_id,cursor)
        elif menu_choice == "2":
          trainer_name = input("Enter in Trainers first and last name: ").title()
          trainer_email = input("Enter trainers email: ")
          add_trainer(trainer_name,trainer_email,cursor)
        elif menu_choice == "3":
          # add_workout_session(member_id, date, duration_minutes, calories_burned)
          member_id = int(input("Enter members I.d. Number: "))
          duration_time = int(input("Enter Duration in Minutes: "))
          calories_burned = duration_time * 3.5
          date = input("Enter Date [YYYY-MM-DD]: ")
          add_workout_sessions(member_id,duration_time,calories_burned,date,cursor)
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
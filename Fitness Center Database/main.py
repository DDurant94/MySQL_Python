import update_data as ud, delete_data as dd, add_data as ad, retrieve_data as rd

print("Welcome to the Fitness Center Database")
while True:
  print("Main Menu:\n1. Add Data\n2. Delete Data\n3. Update Data\n4. View Data\n5. Exit")
  main_menu = input("Choose A Menu Option: ")
  if main_menu == "1":
    ad.main_add()
  elif main_menu == "2":
    dd.main_delete()
  elif main_menu == "3":
    ud.main_update()
  elif main_menu == "4":
    rd.main_retrieve()
  elif main_menu == "5":
    break
  else:
    print("Invalid Option")
  
contacts_name = ['Barry','Daniel','Amrit', 'Krish']
contacts_number = ['7819576042', '7816289223','6178482326','7814239782']
print('Press 1 to search by name')
print('Press 2 to search by phone number')
answer = input()
if answer == '1':
  print("Search by name:")
  name_search = input()
  if name_search == contacts_name[0]: 
    print(contacts_number[0])
  elif name_search == contacts_name[1]:
    print(contacts_number[1])
  elif name_search == contacts_name[2]:
    print(contacts_number[2])
  elif name_search == contacts_name[3]:
    print(contacts_number[3])
  else:
    print('Contact not found')
    print('Add a new contact name:')
    new_name = input()
    print('Enter a new contact number')
    new_number = input()
    contacts_name.append(new_name)
    contacts_number.append(new_number)
    print(contacts_name)
    print(contacts_number)
elif answer == '2':
  print('Search by number:')
  number_search = input()
  if number_search == contacts_number[0]:
    print(contacts_name[0])
  elif number_search == contacts_number[1]:
    print(contacts_name[1])
  elif number_search == contacts_number[2]:
    print(contacts_name[2])
  elif number_search == contacts_number[3]:
    print(contacts_name[3])
  else:
    print('You do not have this number saved in you contacts. Search by name please')
else:
  print('Sorry I do not understand what you are trying to type. Please try again')
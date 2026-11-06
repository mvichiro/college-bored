def create_board(): #O(1)
  board = {
    "ToDo": [],
    "Doing": [],
    "Done": []
  }
  return board

def new_id(board): #O(n)
  id = 0
  for i in board["ToDo"]:
    id += 1
  for i in board["Doing"]:
    id += 1
  for i in board["Done"]:
    id += 1
  return id

def add_card(board, title, description, due, assignee, labels): #O(1)
  card = {
    "id": new_id(board),
    "title": title,
    "description": description,
    "due date": due,
    "assignee": assignee,
    "labels": labels
  }
  board["ToDo"].append(card)
  return card

def move_card(board, source, target, index): #O(1)
  try:
    source_list = board[source]
    target_list = board[target]
    target_list.append(source_list.pop(index))
  except KeyError:
    print("Error: Invalid source or target list name.")
  except:
    print("")

def search_by_title(board, text): #O(n)
  for card in board["ToDo"]:
    if card["title"] == text:
      return ("ToDo", card)
  for card in board["Doing"]:
    if card["title"] == text:
      return ("Doing", card)
  for card in board["Done"]:
    if card["title"] == text:
      return ("Done", card)
  print("No cards found")

def filter_by_assignee(board, name): #O(n)
  filtered_cards = []
  for card in board["ToDo"]:
    if card["assignee"] == name:
      filtered_cards.append(("ToDo", card))
  for card in board["Doing"]:
    if card["assignee"] == name:
      filtered_cards.append(("Doing", card))
  for card in board["Done"]:
    if card["assignee"] == name:
      filtered_cards.append(("Done", card))
  if filtered_cards == []:
    print("No cards found")
  return filtered_cards

def filter_by_label(board, label): #O(n)
  filtered_cards = []
  for card in board["ToDo"]:
    if label in card["labels"]:
      filtered_cards.append(("ToDo", card))
  for card in board["Doing"]:
    if label in card["labels"]:
      filtered_cards.append(("Doing", card))
  for card in board["Done"]:
    if label in card["labels"]:
      filtered_cards.append(("Done", card))
  if filtered_cards == []:
    print("No cards found")
  return filtered_cards

def get_id(card):
  return card["id"]

def cards_in_id_order(board): #O(nlogn)
  cards = []
  for card in board["ToDo"]:
    cards.append(card)
  for card in board["Doing"]:
    cards.append(card)
  for card in board["Done"]:
    cards.append(card)
  return sorted(cards, key=get_id)

def find_card_by_id(cards, card_id): #O(logn)
  if card_id > len(cards)-1:
    return None
  low, high = 0, len(cards)-1
  while low <= high:
    mid = (low+high)//2
    if cards[mid]["id"] == card_id:
      return cards[mid]
    elif cards[mid]["id"] < card_id:
      low = mid + 1
    else:
      high = mid - 1

def sort_by_due(cards): #O(n^2)
  n = len(cards)-1
  for i in range(n):
    for j in range(n-i):
      if cards[j]>cards[j+1]:
        cards[j], cards[j+1] = cards[j+1], cards[j]
  return cards
  
board = create_board()
add_card(board, "test", "test", "oct 11", "Ron Rodillas", [])
add_card(board, "testA", "testA", "oct 11", "Not Ron Rodillas", [])
move_card(board, "To", "Doing", 1)
print(board)

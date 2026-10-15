def create_board():
  board = {
    "ToDo": [],
    "Doing": [],
    "Done": []
  }
  return board

def new_id(board):
  id = 1
  for i in board["ToDo"]:
    id += 1
  for i in board["Doing"]:
    id += 1
  for i in board["Done"]:
    id += 1
  return id

def add_card(board, title, description, due):
  card = {
    "id": new_id(board),
    "title": title,
    "description": description,
    "due date": due
  }
  board["ToDo"].append(card)
  return card

def move_card(board, source, target, index):
  try:
    source_list = board[source]
    target_list = board[target]
    target_list.append(source_list.pop(index))
  except KeyError:
    print("Error: Invalid source or target list name.")
  except :
    print("")
  
board = create_board()
add_card(board, "test", "test", "oct 11")
add_card(board, "testA", "testA", "oct 11")
move_card(board, "To", "Doing", 1)
print(board)

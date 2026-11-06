def show_board(board):
  print("ToDo:")
  for card in board["ToDo"]:
    print(f"{card["title"]}: {card["description"]}.\nDue {card["due date"]} for {card["assignee"]}.\nLabels: {card["labels"]}")
  print("\nDoing:")
  for card in board["Doing"]:
    print(f"{card["title"]}: {card["description"]}.\nDue {card["due date"]} for {card["assignee"]}.\nLabels: {card["labels"]}")
  print("\nDone:")
  for card in board["Done"]:
    print(f"{card["title"]}: {card["description"]}.\nDue {card["due date"]} for {card["assignee"]}.\nLabels: {card["labels"]}")

def main():
  running = True
  while running:
    print("Actions: [1] quit")
    action = input("What Action would you like to do?")
    if action == "1":
      running = False

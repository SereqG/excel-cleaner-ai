from process_manager.file_handling import File
from process_manager.action_handling import Action

def app():
  file = File()
  while True:
    file.load_file()
    print(file.is_file_loaded)
    if file.is_file_loaded == True:
      action = Action(file.df)
      action.select_possible_actions



if __name__ == "__main__":
  app()


import pandas

class File:
  def __init__(self):
    self.is_file_loaded = False
    
  def load_file(self):
    path = input("Enter the path to your excel file: ")
    try:
      df = pandas.read_excel(path)
      self.df = df
      self.is_file_loaded = True
      print("File loaded successfully!")
    except:
      print("Something went wrong, try again")

  def show_path(self):
    print(self.path)

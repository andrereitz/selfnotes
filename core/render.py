import os
from tabulate import tabulate
from typing import Self
from beaupy import prompt, select_multiple, confirm

class Render:
  def __init__(self, store) -> None:
    self._store = store
    
  
  def show_items(self: Self) -> None:
    
    if len(self._store.items) > 0:
      filtered = [{"completed": 'X', "title": self.strike_text(item["title"])} if item["completed"] == 'true' else {"completed": '', "title": item["title"]} for item in  self._store]
      headers = {"completed": "Status", "title": "Task"}
      print(tabulate(sorted(filtered, key=lambda x: (x["completed"], x["title"])), headers=headers))
    
    else:
      print("You have no list items, create a new one pressing [n]")
    
  
  def mark_completed(self: Self) -> None:
    self.clear()
    
    items = [item for item in self._store if item["completed"] == 'false']    
    selected = select_multiple(options=items, preprocessor=lambda x: x["title"])
    ids = [item["id"] for item in selected]
    
    self._store.items_completed(ids)
    
    self.show_items()
    

  def mark_uncompleted(self: Self) -> None:
    self.clear()
    
    items = [item for item in self._store if item["completed"] == 'true']
    
    selected = select_multiple(options=items, preprocessor=lambda x: x["title"])
    ids = [item["id"] for item in selected]
    
    self._store.items_uncompleted(ids)
        
    self.show_items()
    
    
  def delete_items(self: Self) -> None:
    self.clear()
    
    items = [item for item in self._store]
    
    selected = select_multiple(options=items, preprocessor=lambda x: x["title"])
    titles = [item["title"] for item in selected]
    ids = [item["id"] for item in selected]
    
    print(f"Deleting: \n- {'\n- '.join(titles)} \n\n")
    if confirm("Are you sure?"):
      self._store.delete_items(ids)
        
    self.show_items()
    
    
  def new_item(self: Self) -> None:
    self.clear()
    
    title = prompt("New item title:")
    self._store.new_item(title)
    
    self.show_items()

  
  @staticmethod
  def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
  @staticmethod
  def strike_text(text) -> None:
    return ''.join([u'\u0336{}'.format(c) for c in text])

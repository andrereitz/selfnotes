import os, json
from typing import Self
import uuid

class Store:
  def __init__(self: Self, name: str = "default") -> Self:
    self.name = name
    self.items = []
    self.path = os.path.join(os.getcwd(), 'data', f"{name}.json")
    self.datadir = os.path.join(os.getcwd(), 'data')
    
    self.init_file()
    
    
  def init_file(self: Self) -> None:    
    if not os.path.exists(self.datadir):
      os.mkdir(self.datadir)
        
    if not os.path.exists(self.path):
      self.save_file()
    else:
      self.read_file()
      
        
  def save_file(self) -> None:
    with open(self.path, "w") as file:
      json.dump({ 'name': self.name, 'items': self.items }, file, ensure_ascii=False, indent=2)
      
        
  def read_file(self) -> None:
    with open(self.path, "r") as file:
      contents = json.load(file)
      self.items = contents["items"]
      
      
  def items_completed(self, ids):
    self.items = [ { "completed": "true" if item["id"] in ids else item["completed"], "title": item["title"], "id": item["id"] } for item in self.items ]
    self.save_file()
    
    
  def items_uncompleted(self, ids):
    self.items = [ { "completed": "false" if item["id"] in ids else item["completed"], "title": item["title"], "id": item["id"] } for item in self.items ]
    self.save_file()
    
  def delete_items(self, ids):
    self.items = [ item for item in self.items if item["id"] not in ids ]
    self.save_file()
        
    
  def new_item(self, title):
    if not title:
      raise ValueError("Title can not be empty")
    
    self.items.append({ "id": str(uuid.uuid1()), "completed": "false", "title": title})
    self.save_file()
    
  
  def __str__(self):
    return f"File instance with {self.name} list"
  
  
  def __iter__(self):
    return iter(self.items)
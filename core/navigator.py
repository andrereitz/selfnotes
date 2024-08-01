import time

class Navigator:
  def __init__(self, render):
    self._render = render
    
    while True:
      self._render.clear()
      self._render.show_items()
      self.print_nav()

      cmd = input("Choose an option: ")
      
      try:
        self.do_navigation(cmd)
        
      except ValueError as err:
        print("\n")
        if err.args:
          print(err, end="\n\n")
        else:  
          print("Invalid options, choose from the navigation", end="\n\n")
          
        time.sleep(2)
        continue
        
      except SystemExit:
        self._render.clear()
        return
  
  def do_navigation(self, cmd):
    print(cmd)
    match cmd:
      case 'n':
        self._render.new_item()
      case 'd':
        self._render.delete_items()
      case 'c':
        self._render.mark_completed()
      case 'x':
        self._render.mark_uncompleted()
      case 'w':
        raise SystemExit
      case _:
        raise ValueError
  
  def print_nav(self):
    print("\n\n [n] New | [d] Delete  \n [c] Completed | [x] Uncompleted \n [w] Exit", end="\n\n")

        
import sys
from core import Store, Render, Navigator

def main():
  if(len(sys.argv) == 1):
    store = Store()
  
  if(len(sys.argv) > 1):
    store = Store(sys.argv[1])

  render = Render(store)
  
  Navigator(render)


if __name__ == "__main__":
    main()
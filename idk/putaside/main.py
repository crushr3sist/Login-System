from api import *
#from gui import *
import sqlite3
from pygame_functions import *

def main():
    
    while True:
        pygame.event.pump()
        if keyPressed('space'):
            break
    endWait()
     
if __name__=="__main__":
    main()




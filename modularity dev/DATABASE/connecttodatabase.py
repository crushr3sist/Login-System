import os, sqlite3
class connectDB:
    def __init__(self):
        self.Path = os.getcwd()+"\database\main_DataBase.db"
        self.con = sqlite3.connect(self.Path)
    def establish(self):
        if self.Path != os.path.islink(self.Path):
            self.con = sqlite3.connect(self.Path)
        if os.path.exists(self.Path) == True:
            #print("database is being created or already exists")
            None
        elif os.path.exists(Path) == False:
            print(fr"Your was created successfully at {os.getcwd()+'/main_DataBase.db'} ")
        return self.con



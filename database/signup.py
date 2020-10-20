class sign_up:
    def __init__(self):
        self.con = connect()
        self.userID = 0
        self.userID = userID + 1
        self.firstName = str(input("enter your first name:"))
        self.lastName = str(input("enter your last name:"))
        self.emailAdd = str(input(r"enter your email address:"))
        self.userName = str(input("enter your desired username:"))
        self.password = str(input("enter your desired password:"))
    def register(self):
        try:
            self.con.execute('''
            INSERT INTO users (userID,firstName,lastName,email,userName,password)
            VALUES (?,?,?,?,?,?)''',
            (self.userID, self.firstName, self.lastName, self.emailAdd,self.userName,self.password)
            )
            self.con.commit()
            self.con.close()
            print("your account has been created :)")
        except Error as e:
            print(e)
        con.execute("SELECT userName, password FROM Users,Admin ")
        cursor = con.cursor()
        fetchAuthData = list(cursor.fetchall())

        print(fetchAuthData)

        if login_Password not in fetchAuthData or login_Username not in fetchAuthData:
            for i in range(0,6):
                print("please try again")
                login_Username = input("enter your username:")
                login_Password = input("enter your password:")
                if login_Password in fetchAuthData or login_Username in fetchAuthData:
                    # check if the entered details belong in the admin or user table
                    print("login sucessful")
                    break
                else:
                    if i >= 5:
                        print("please try again later")
                        break
        if login_Password in fetchAuthData and login_Username in fetchAuthData:
            print("Login Sucessful")          
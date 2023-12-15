from database_part import DataBasHelper


class OnlineShop:
    def __init__(self):
        self.database = DataBasHelper()
        self.menu()

    def menu(self):
        print(""" 
                1. Enter 1 for register
                2. Enter 2 for login
                3. Enter 3 to show the database
                4. Enter anything to exit
                 """)
        input_key = input("Please enter here : ")
        if input_key=="1":
            self.register()
        elif input_key=="2":
            self.login()
        elif input_key=="3":
            self.database.show_database()
        else:
            print("invalid key!")

    def register_domain_inputer(self):

        id = int(input("Input the id number : "))
        name = input("Enter name : ")
        email = input("Enter email : ")
        password = input("Enter password : ")

        return id, name, email, password
        
        
    def register(self):

        id, name, email, password = self.register_domain_inputer()
        
        try:
            result = self.database.register_database(id, name, email, password)
        except:
            print("some error occured")
        else:
            if result==1:
                print("Register Successfull")
            else:
                print("Register Failed")


    def login_domain_inputer(self):

        email = input("Enter your email : ")
        password = input("Enter your password : ")

        return email, password

    
    def login(self):
        email, password = self.login_domain_inputer()
        try:
            data = self.database.login_database(email, password)
        except:
            print("Error occured")
        
        if len(data)!=0:
            print("login Successfull")
            print(data)
        else:
            print("You are not registered")


user1 = OnlineShop()
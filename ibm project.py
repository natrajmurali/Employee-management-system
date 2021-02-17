class EmployeePortal():
    def __init__(self,username,password,DOB,Bloodgroup,setusername,setpassword,mobileno,email,listEmployee,EmpID,searchID):
        self.EnterUsername=username
        self.EnterPassword=password
        self.EnterDOB=DOB
        self.Bloodgroup=Bloodgroup
        self.SetUsername=setusername
        self.SetPassword=setpassword
        self.EnterMobileno=mobileno
        self.EnterEmail=email
        self.ListEmployee=listEmployee
        self.employeeID=EmpID
        self.searchEmployee=searchID



       
class signup():
    def __init__(self,name,DOB,Bloodgroup,setuser,setpassword,mobileno,email):
        self.name=name
        self.DOB=DOB
        self.Bloodgroup
        self.setusername=setusername
        self.setpassword=setpassword
        self.mobileno=mobileno
        self.email=email
        
while (True):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to Employee Portal System ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("[1] login \n")
    print("[2] Register \n")
    print("[3]Export Employees")
    user_option = input("Please select option:")
    if user_option not in ['1','2','3']:
        print("Please enter valid option")
        continue
    else:
        user_option=int(user_option)
    if user_option == 1:
        print(input('Enter username:'))
        print(input("Enter password:"))
        print(input("Enter DOB:"))
    elif user_option == 2:
            print("Enter the details below to sign up!")
            name=input("Enter name:")
            DOB =input('Enter DOB:')
            Bloodgroup=input('Enter Bloodgroup')
            SetUsername=input('Setusername:')
            SetPassword=input('Setpassword:')
            mobileno=input('Enter Mobileno:')
            email=input('Enter email:')
    elif user_option == 3:
        with open("file2.txt", "w") as output:
            output.write(str(ListEmployee))


        
        
    def ListEmployee():
        ListEmployee.append([name,DOB,Bloodgroup,SetUsername,SetPassword,mobileno,email])





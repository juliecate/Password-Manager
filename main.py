import random
import string


print("\nPASSWORD MANAGER \n")

# Login to password manager first


system = True
while system:
  user_name = input("User Name: ")
  user_pw = input("Password: ")
  user = user_name + user_pw

  with open("login.txt") as login_file:
    login = read.login_file()
    if user in login:
      print("Login successfull.\n Hello" + user_name)
      system = False
    else: 
      print("Login failed. Please ask your admin to get registered on the system.")
  

  


# Create text file to store and check credentials
# Proceed only if logged in

# Ask what the program should do
print("What would you like to do?")
print(" 1   Create a new password\n 2   Store login details\n 3   Search for login details\n")
task = int(input("Please enter the number of the corresponding task: ")) 

# 1   Create a new password
if task == 1:
    print(" 1   Create a new password\n")
    pw_length = int(input("How many characters does your password need? "))

    # Create a random password based on lower and upper case letters, digits, punctuation and length
    def create_pw(pw_length):
        available_char = string.ascii_letters + string.digits + string.punctuation
        global new_password 
        new_password = ""

        for i in range(pw_length):  
            new_password += random.choice(available_char)
            i = i+1
        print("This is your new password: " + new_password)
    
    create_pw(pw_length)
    
    
    # Ask to store the generated password
    pw_to_store = input("\nDo you want to store this password?")
    s = True
    while s:
        if pw_to_store == "yes":
            task = 2
            s = False
        elif pw_to_store == "no":
            s = False
        else: 
            pw_to_store = input("Your answer is not valid. Please select yes or no: ")


# 2   Store login details
if task == 2: 
   print("2   Store login details\n") 
   
   # Ask for a keyword as identifier to store user name and pw under
   identifier = input("Please enter a keyword, which will help you to identify your login details: ")
   user_name = input("Please enter your user name: ")
   password = input("Please enter your password: ")
   
   login_list = [identifier, user_name, password]

   # Login details to be stored in a dictionary
   def login_details(login_list):
     
       global login_str
       login_str = ""
       login_str.join(login_list)
       txt_file = open("pw_storage.txt", "w")
       txt_file.write(login_str)
       txt_file.close()
       

   login_details(login_list)


# 3   Search for login details
if task ==3: 
  print("3   Search for login details\n")
  
  search_login = input("Please enter the keyword for the login you are looking for: ")
  # open and search for login details in txt file
  searchfile = open("pw_storage.txt", "r")
  for line in searchfile:
    if search_login in line:
      print(line)
    else:
      print("No login has been stored!")
  searchfile.close()



# Search for a pw
# Store a pw with user name


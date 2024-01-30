def Options(): #to define option
    #we print the following that will serve as an option of the users
    print("""
Options:
[1] Join Juan(Add a member)
[2] View a Juan's record
[3] View all members
[4] Edit Juan's weight
[5] Delete Juan's record
[6] Delete all member records
[7] Save to file
[8] Load from file
[0] Exit""")
    choice = int(input("Choice: ")) #after printing the options, we ask the user about their choice
    return choice #so it will return the choice 

def Add(count): #to define add members
    name = input("Enter name: ") #ask users for the name,
    weight = float(input("Enter weight (kg): ")) #weight and 
    height = float(input("Enter heigth (cm): ")) #height
    bmi = weight / (height / 100) ** 2 #this is the calculation of the BMi
    BMI = round(bmi, 1) #to get only the first decimal point of the bmi, we use the round operation
    print("\n--------------------------------------------------")
    print("Welcome, " + name + "!\nYour BMI is " + str(BMI), 'and your type is ' + str(result(BMI))) #to tell the user the BMI and type of their inputs, this is the ouput
    print("--------------------------------------------------\n")
    data = {} #we set an empty dictionary named as data
    data['Name'] = name #we input a key of Name for the value of name
    data['Weight'] = weight #input a key of Weight for the value of weight
    data['Height'] = height #input a key of Height for the value of height
    data['BMI'] = BMI #input a key of BMI for the value of bmi and
    data['Type'] = result(BMI) #input a key of Type for the value of result(BMI)
    Information[memberid(count)] = data #we input the dictionary of data into the dictionary of Information using the key of memberid(count)
    return "" #returns an empty string


def memberid(count): #for the incrementation of the Member id
    if count < 10: #if the count is less than 10
        member_id = 'M00' + str(count) #member_id will be M00 plus the string of the count
    elif count >= 10 and count < 100: #if the count is greater than or equal to 10 and less than 100
        member_id = 'M0' + str(count) #the member_id is will be M0 plus the string of the count. It is M0 because the count is 2 digit
    elif count >= 100: #if the count is greater than or equal to 100
        member_id = 'M' + str(count) #the member_id will be M plus the string of the count. Since count is 3 digit in this case, we only add M to it
    return member_id #and so it will return the member_id

def result(BMI): #to define the result of the bmi
    if BMI < 18.5: #if bmi results in the calculation is less than to 18.5
        tayp = "Underweight" #the tayp will be underweight
    elif BMI > 18.5 and BMI < 25: #if the bmi is greater than 18.5 and less than 25
        tayp = "Normal" #the tayp will be normal
    elif BMI > 25 and BMI < 30: #if the bmi is greater than 25 and less than 30
        tayp = "Overweight" #the tayp is overweight
    elif BMI >= 30: #if the bmi is greter than or equal to 30
        tayp = "Obese" #the tayp is obese
    return tayp #it will return the tayp

def ViewMember(Information): #to define view member
    member_id = input("Enter member id: ") #we aks users for the member id it wants to see
    for k in Information: #in every k in Information
        if member_id == k: #if member_id is equal to k then we set 
            content = Information[k] #content variable to Information[k] to easily access the another key-value of the disctionary
            print("\n=== Member Information ===\n"+"("+ k +") " + content['Name'], content['Weight'], 'kg', content['Height'], 'cm' + " (BMI:"+ str(content['BMI']) + ';' + str(content['Type']) + ')')
            break #it will terminate the block of codes in view member
    else: #however, if the member_id users input is not equal in the k in Information
        print("Member Id does not exist") #we tell the user that the member id does not exist
        return "" #it will return an empty string

def ViewAll(): #to define the view all 
    print("\n=============== List of members ==================\n") #list of members will be printed out 
    count = 0 #we set count initialization
    for k in Information: #in every k in Information
        content = Information[k] #we set content variable as Information[K] to access its another key-values in the dictionary
        for i in range(len(Information)): #every i in range of count of Information dictionary, we update the count as
            count += 1 #adding 1 to it, the count will be used in printing out the list of members
            print(str(count) + "." + "("+ k +") " + content['Name'], content['Weight'], 'kg', content['Height'], 'cm' + " (BMI:"+ str(content['BMI']) + ';' + str(content['Type']) + ')') 
            break #and so we terminate the code of block for the view all
    print("\n==================================================")
    return "" #it will return an empty string
       
def Edit(Information): #to define the edit options
    member_id = input("Enter member id: ") #users will be asked about the member is they want ot edit
    for k in Information: #for every keys in Information dictionary
        if member_id == k: #if the member_id is equal to k or keys, it will ask the user about the new weight
            edit_weight = float(input("Please input the new weight: "))
            new_info = Information[k] #we set new_info as the Information[k] or the key of the Information
            new_info["Weight"] = edit_weight #to replace the old value of "Weight" in the dictionary, we access the weight by using the new_info and input the new value for weight
            height = new_info["Height"] #we set the variable height as the height in the dictionary of the k
            bmi = edit_weight / (float(height) / 100) ** 2 #the calculation of the bmi
            BMI = round(bmi, 1) #to make the BMI in its 1st decimal point only, we use the round opreation
            new_info["BMI"] = BMI #to replace the old value of the BMI in the Information[k]
            new_info["Type"] = result(BMI)#to replace the old value of the Type in the Information [k]
            print(new_info['Name'], new_info['Weight'], 'kg', new_info['Height'], 'cm' + " (BMI:"+ str(new_info['BMI']) + ';' + str(new_info['Type']) + ')') 
            break #after the process, the Edit(Information) block of codes will be terminate
    else: #however, if the member_id users input is not in the dictionary, it will tell the user that
        print("Member Id does not exist") #the member id does not exist
    return "" #the def Edit(Information) returns an empty string

def DelMember(Information): #to define the delete member
    member_id = input("Enter member id: ") #it will ask the user what's member if they want to be deleted
    if member_id in Information: #if the member_id is in Information dictionary 
        print('Member ' + member_id + ' successfully deleted.') #and so will tell the user that it has been successfully deleted
        del Information[member_id] #it will be deleted in the Information using the del operation
    else: #however, if the member_id users input is not in the dictionary
        print('Sorry the record does not exit') #it will tell the user that the record does not exist
    return "" #it will return an empty string
    
def DelAll(): #to define the delete all
    print("All entries successfully deted.") #after deleting, it will return this statement to tell the user that the contents of dictionary has been deleted
    Information.clear() #to delete all the contents of the dictionary of Information, we use the operation .clear
    return ""

def SaveToFile():
    filehandle = open("Sparrow's Gym.txt", "w")
    for k in Information:
        data = Information[k]
        name = data['Name']
        weight = data['Weight']
        height = data['Height']
        bmi = data['BMI']
        tayp = data['Type']
        filehandle.write(k + "-" + name + "-" + str(weight) + "-" + str(height) + "-" + str(bmi) + "-" + str(tayp) + "\n")
    print("Successfully saved to file ("+str(len(Information))+" entrie/s)" )
    filehandle.close()
    
def LoadFromFile():
    filehandle = open("Sparrow's Gym.txt", "r")
    Information.clear
    for line in filehandle:
        detail = line[:-1].split("-")
        data = {}
        data['Name'] = detail[1]
        data['Weight'] = detail[2]
        data['Height'] = detail[3]
        data['BMI'] = detail[4]
        data['Type'] = detail[5]
        Information[detail[0]] = data
    print("Successfully loaded entries from file ("+str(len(Information))+" entrie/s)")
    filehandle.close()
        
def choice(): #for the choice of users, we set an
    choice = "" #empty string for choice
    count = 0 #set an initialized for count
    while True: #while True
        choice = Options() #we set choice as the function call for Options()
        if choice == 1: #if the users choice is equal to 1, we update the initialization for
            count += 1 #count by adding 1 to it, it means that this is the count of how many times user adds to the dictionary
            Add(count) #function call for Add(count)
            continue #after proceeding to Add(count), this simply tells that the program should continue asking users for choice 
        elif choice == 2: #if the users choice is equal to 2, we call 
            ViewMember(Information) #the ViewMember(Information)
            continue #this simply tells that the program should continue asking users for choice 
        elif choice == 3: #if the users choice is equal to 3, we call the 
            ViewAll() #the ViewAll()
            continue #this simply tells that the program should continue asking users for choice 
        elif choice == 4: # if the users choice is equal to 4, we call the 
            Edit(Information) #the Eidt(Information)
            continue #this simply tells that the program should continue asking users for choice 
        elif choice == 5:#if the users choice is equal to 5, we call 
            DelMember(Information) #the DelMember(Information)
            continue #this simply tells that the program should continue asking users for choice 
        elif choice == 6: #if the users choice is equal to 6, we call 
            DelAll() #the DelAll()
            continue #this simply tells that the program should continue asking users for choice 
        elif choice == 7: #if the users choice is equal to 7, we call
            SaveToFile() #the SaveToFile()
            continue #this simply tells that the program should continue asking users for choice 
        elif choice == 8: #if the users choice is equal to 8, then we call the
            LoadFromFile() #LoadFromFile() function
            count += len(Information) #this is for the incrementation that would be used for the member_id
            continue #this simply tells that the program should continue asking users for choice 
        elif choice == 0: #if the choice of the user is 0
            print('\nThank you for using this program!') #this will be printed and tell the user thank you 
            break #therefore, once the user choice is 0, the program will be terminate
        else: #However, if the users choice is not in the choices
            print('Invalid input') #it will tell the users that they have invalid input
    return "" #returns an empty string
 
Information = {} #to localized the dictionary of Information
print("""\n
    =!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!\n
          Welcome to HeavenlyHomes Club :>\n
      Where you can find peace while you do a fit!
         Be Juan of us to be physically fit!\n
    =!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!
      """)
print(choice()) #function call for choice()

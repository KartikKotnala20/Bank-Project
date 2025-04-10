import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

print("database connected successfully")

# cursor.execute(""" CREATE Table Customer_Details
#                (id INTEGER primary key AUTOINCREMENT,
#                Name varchar(32),
#                account_num INTEGER UNIQUE NOT NULL ,
#                account_type varchar(20),
#                balance number default(500),
#                branch varchar(20),
#                phone_num number(10),
#                email_id varchar(40),
#                Gender char(6),
#                pin number(4)) """)

print("Table created successfully")

def createAccount():
  print("Enter the below details: ")
  
  Name=input("Enter your name :")
  account_num=input("enter your account number:")
  account_type=input("enter the account type: ")
  branch=input("enter your branch: ")
  phone_num=input("enter your phone number: ")
  email_id=input("enter your email: ")
  Gender=input("Enter your Gender: ")

  cursor.execute(f'''insert into Customer_Details(Name,account_num,account_type,branch,phone_num,email_id,Gender)
                 values("{Name}",{account_num},"{account_type}","{branch}",{phone_num},"{email_id}","{Gender}")''')
  conn.commit()

def pin_generation():
  print(" Pin Generation ")
  account_num=int(input("enter the account number : "))
  value=cursor.execute(f''' select * from Customer_details where account_num={account_num}''')
  data=value.fetchone()
  if data is not None:
    try:
      pin=int(input("enter the pin :"))
      con_pin=int(input("enter the pin again :"))
      if pin == con_pin:
        length = str(pin)
        if len(length) ==4:
          cursor.execute(f''' update Customer_details set pin = {pin} where account_num ={account_num};''')
          conn.commit()
          print("pin generated successfully, never share with anyone")
        else:
          print("enter the pin with 4 digits")
      
    except Exception as e:
      print(f"enter the number only{e}")


  else:
    print("please enter valid account number")


def check_bal():
  account_num= int(input("enter the acc"))
  pin=int(input("enter the pin"))
  cursor.execute(f''' select * from Customer_details where
  account_num={account_num}''')
  a= cursor.fetchone()
  if a is not None:
    if pin == a[-1]:
      print(a[4])

    else:
      print("pin is not valid")
  else:
    print('pleade enter the valid account number bcz, the entered acc details is not present in db')


def withdrawl():
  account_num=int(input("enter your account number :"))
  cursor.execute(f''' select * from Customer_details where account_num ={account_num} ''')
  data=cursor.fetchone()
  if data is not None:
    pin=int(input("enter your pin:"))
    if pin ==data[-1]:
      if data[4]<=500:
        print("you have minimum balance in your account\n and you are unable proceed")
      else:
        print("please enter valid pin")
    else:
      print("please enter a valid account number")


def deposite():
  account_num=int(input("enter your account number :"))
  cursor.execute(f''' select * from Customer_details where account_num ={account_num} ''')
  data=cursor.fetchone()
  if data is not None:
    pin=int(input("enter your pin:"))
    if pin ==data[+1]:
      if data[4]<=500:
        print("you have minimum balance in your account\n and you are unable proceed")
      else:
        print("please enter valid pin")
    else:
      print("please enter a valid account number")


def transfer():
  print()
  print("---Account Transfer-----")
  ac_num = int(input("enter your account number: "))
  cursor.execute(f""" select * from Customer_details where account_num = {ac_num} """)
  data =cursor.fetchone()
  if data is not None:
    rev_ac=int(input("enter reciever account number: "))
    cursor.execute(f""" select * from Customer_details where account_num = {rev_ac} """)
    data1= cursor.fetchone()
    if data1 is not None:
      amt = int(input("enter amount to trasfer: "))
      pin = int(input("enter your pin: "))
      if pin == data[-1]:
        sender_bal = data[4]-amt
        cursor.execute(f""" update Customer_details set balance = {sender_bal} where account_num={ac_num} """)
        conn.commit()
        rev_bal=data1[4]+amt
        cursor.execute(f""" update Customer_details set balance ={rev_bal} where account_num={rev_ac} """)
        conn.commit()
        print(f"{amt} is successfully transffered from your account num is {ac_num} to the reciever account number is {rev_ac} and your aval")
      else:
        print("pin is inncorrect")
    else:
      print("please enter a valid account")
  else:
    print("enter a valid account number")


while True:
  print(" Enter 1 for account creation \n please enter 2 for pin generation \n please enter 3 for check balance \n please enter 4 for withdrawl  \n enter 5 for deposite \n enter 6 for  account transfer \n enter exit for closing the program")
  opt=input("Please select the command : ")
  if opt=="1":
    createAccount()
  elif opt=="2":
    pin_generation()
  elif opt=="3":
    check_bal()
  elif opt=="4":
    withdrawl()
  elif opt=="5":
    deposite()
  elif opt=="6":
    transfer()
  elif opt=="Exit":
    break
  else:
    print("enter a valid point")









      
    
    
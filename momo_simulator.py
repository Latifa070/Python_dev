#function that displays the maing momo menu
def display_menu():
  main_menu = {
                "1)": "Transfer Money",
                "2)": "MOMOPay& Pay Bill",
                "3)": "Transfer Money",
                "4)": "Airtime and Bundles",
                "#":   "For Next"
          } 
  for key, value in main_menu.items():
     print(f"{key} {value}")


  
#function that displays the rest of the menu when the user selects the # for next option
def display_next_menu():
  next_menu ={ 
               "6)": "My Wallet",
               "7)":"Just4u (offers for you) ",
               "8)": "MOMO App (300MB for free) "
   }
  for key, value in next_menu.items():
        print(f"{key} {value}")

# creating the transfer function 
def transfer_options():
    main_menu ={
              "1)": "MoMo User",
              "2)": "Non-MOMO User",
              "3)": "Send with care",
              "4)": "Favorite ",
              "5)": "Other Networks",
              "6)": "Bank Acounts",
              "#":  "For Next"      
    }
    for key, value in main_menu.items():
        print(f"{key} {value}")

def transfer_next_options():
    
   
# prompting the user for the input

ussd = input("Enter the USSD : ")
if ussd != "*170#":
        print("Invalid usssd ")
        

else:
    print("select an option ")
    option = input(display_menu())
    

    


  

      

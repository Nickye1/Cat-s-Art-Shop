# import random to use python function random.choice() to randomize resetPasswordQuestions during account creation 
import random
# stores all search results that match the user's search
searchedProduct = []
# stores username user makes during account creation 
usernameList = []
# stores password user makes during account creation 
passwordList = []
# stores recovery questions
resetPasswordQuestions = ["How old are you?", "What is your favourite TV show?","What is your favourite book?", "What is your birthday month?","What is your favourite colour?", "What is your favourite season?","Are you a morning person or night person?","Are you an apple user or android?","What did you want to be when you were younger?","What is your favourite subject?"]
# stores recovery questions asked during account creation
askedResetPasswordOptions = []
# stores answers to recovery questions asked during account creation 
resetPasswordAnswers = []
# Master catalog of all 100 products 
masterCatalog = [ 100 products for sale]
# stores all items that are purchased
shoppingCart = []
# stores the quantity of each item purchased
quantityOfItemsPurchased = []

'''
Creating the Welcome Screen to the website. Displays password requirements needed to create an account. Function links to accountCreation() to being account creation process.
'''
def welcomeScreen():
  # Printing a welcome message stating information to make account
  print("\n✧･ﾟ: *✧･ﾟ:* 🎨 Welcome to Cat's Art Store! *:･ﾟ✧*:･ﾟ✧\n\nPlease create your username and password for your new account.Your password must include:\n✧ Lowercase Letter\n✧ Uppercase Letter\n✧ Number\n✧ Special character (!@#$%^&*:;)\n✧ 8-12 characters in length")
  # Going to accountCreation function to begin username and password creation
  print(accountCreation())

'''
Prompting user to create a username and password. The username and password is stored in usernameList = [] and passwordList = [] to later be used in login system. The password has to meet the requirements stated in welcome screen. If the password doesn't meet the requirements, it will print out the requirements that aren't met. After account creation, 3 recovery questions will be asked and the questions and answers will be stored in askedResetPasswordOptions = [] and resetPasswordAnswers = []
'''
def accountCreation():
  # clearing usernameList incase user has to create another account
  usernameList.clear()
  # clearing passwordList incase user has to create another password
  passwordList.clear()
  # printing a header
  print("\n━━━━━━━━━━━━━━━━ 🎨 Account Creation ━━━━━━━━━━━━━━━━")
  # prompting user to make a username
  createUsername = (str)(input("Create username: "))
  # prompting user to make a password
  createStrPass = input("Create password: ")
  # declaring all the cases of uppercase letters
  upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # declaring all the cases of lowercase letters
  lowerCase = "abcdefghijklmnopqrstuvwxyz"
  # declaring all the cases of numbers
  digits = "1234567890"
  # declaring all the cases of special characters
  special = "!@#$%^&*:;"
  # declaring isUpper as false 
  isUpper = False
  # declaring isLower as false 
  isLower = False
  # declaring isDigits as false 
  isDigits = False
  # declaring isSpecial as false 
  isSpecial = False
  # Using a for loop to check every character in the password. If th
  for i in range(0, len(createStrPass)):
    # if there is an uppercase letter in the password, isUpper changes from false to true
    if upperCase.find(createStrPass[i]) >= 0:
      isUpper = True
    # if there is a lowercase letter in the password, isLower changes from false to true
    if lowerCase.find(createStrPass[i]) >= 0:
      isLower = True
    # if there is a number in the password, isDigits changes from false to true
    if digits.find(createStrPass[i]) >= 0:
      isDigits = True
    # if there is a special character in the password, isSpecial changes from false to true
    if special.find(createStrPass[i]) >= 0:
      isSpecial = True
    # if there isn't an uppercase letter in the password, the requirement message will print
  if isUpper == False:
    print("Uppercase requirement not met")
    # if there isn't a lowercase letter in the password, the requirement message will print
  if isLower == False:
    print("Lowercase requirement not met")
    # if there isn't a number in the password, the requirement message will print
  if isDigits == False:
    print("Number requirement not met")
    # if there isn't a special character in the password, the requirement message will print
  if isSpecial == False:
    print("Special Character requirement not met")
    # if the password length is not between 8-12, the requirement message will print
  if len(createStrPass) < 8 or len(createStrPass) > 12:
    print("Length requirement not met")
    # checks if isUpper = True, isLower = True, isDigits = True, isSpecial = True, and if the password length is between 8-12 characters... (All password requirements are passed) 
  if isUpper and isLower and isDigits and isSpecial and len(
      createStrPass) >= 8 and len(createStrPass) <= 12:
    # stores the username into usernameList = [] to be used later to check in login system 
    usernameList.append(createUsername)
    # stores the password into passwordList = [] to be used later to check in login system 
    passwordList.append(createStrPass)
    # printing account creation success message and prompting user to answer 3 random recovery account questions
    print("Account Creation Success!\n\nJust before you login, Please answer the following recovery questions.")
    # for loop repeats the user to answer 3 different questions
    random.shuffle(resetPasswordQuestions)
    for i in range(0, 3):
      # storing the random question from resetPasswordQuestions = [] into a variable
      question = resetPasswordQuestions[i]
      # printing the random question
      print(question)
      # prompting user to answer the question 
      questionAnswer = input("Answer: ")
      # storing the questions asked into askedResetPasswordOptions = [] to later be used in login if needed
      askedResetPasswordOptions.append(question)
      # storing the answers to the questions asked into resetPasswordAnswers = [] to later be used in login if needed
      resetPasswordAnswers.append(questionAnswer)
      # Going to loginSystem function to being login
    loginSystem()
  # if any of the password conditions aren't met, return to account creation
  else:
    return accountCreation()

'''
Prompting user to login using the created username and password. If the login information is correct they can be start shopping. Otherwise, if the login information is incorrect after 3 tries, the recovery questions will be printed and the program will prompt the user for the answers. If the answers do not match with the answer they gave during account creation, the program will ask the user to make a new account. 
'''
def loginSystem():
  # printing login centre heading
  print("━━━━━━━━━━━━━━━━ 🎨 Login Centre ━━━━━━━━━━━━━━━━")
  # declaring incorrectPasswordCounter as 0. This counter keeps track of the amount of times the user entered the wrong password. When this counter reaches 3, the program will start asking recovery questions. 
  incorrectPasswordCounter = 0
  # declaring successfulLogin as 0. When the user logins with the correct account information, this counter will change to 1 which is the key to shopping
  successfulLogin = 0
  # printing welcome to login centre message and instructions for user
  print("Welcome to Cat's Login Centre! Please enter your account information below:\n")
  # if the conditions successfulLogin != 1 and incorrectPasswordCounter != 3 aren't met, then the while loop will break. 
  while successfulLogin != 1 and incorrectPasswordCounter != 3:
    # prompting user to input their username
    authUsername = input("Username:")
    # prompting user to input their password
    authStrPass = input("Password:")
    # checking if the username entered is the same as the username stored in usernameList and checking if the password is the same as the password stored in passwordList
    if usernameList[0] == authUsername and passwordList[0] == authStrPass:
      # change successfulLogin = 1
      successfulLogin = 1
      # printing successful login message
      print("Successful Login!")
      # otherwise, + 1 to incorrectPasswordCounter and print unsuccessful login message
    else:
      incorrectPasswordCounter = incorrectPasswordCounter + 1
      print("Unsuccessful Login\n")
  # if successful login == 1, go to function catalogShopping() to start shopping
  if successfulLogin == 1:
    catalogShopping()
  # otherwise, start recovery question process
  else:
    # declaring the number of correct questions answered
    correctQuestion = 0
    # printing recovery question intstructions and message 
    print("You have entered the wrong account information 3 times. Please answer the following recovery questions. ")
    # repeats questions asked if answer does not match the one entered in account creation. When correctQuestion = 3, the loop breaks and the user can start shopping. 
    while correctQuestion != 3:
      # printing the question stored in askedResetPasswordOptions 
      print(askedResetPasswordOptions[correctQuestion])
      # prompting the user to answer their answer to the question 
      askedResetQuestionAnswer = input("Answer: ")
      # comparing the answer entered during account creation to answer during recovery question. If the answer is the same, we + 1 to correctQuestion = 0 
      if askedResetQuestionAnswer == resetPasswordAnswers[correctQuestion]:
        correctQuestion = correctQuestion + 1
      # comparing the answer entered during account creation to answer during recovery question. If the answer is the not the same, print wrong answer message and have user make a new account
      elif askedResetQuestionAnswer != resetPasswordAnswers[correctQuestion]:
        print("Your answer is wrong. Make a new account.")
        welcomeScreen()

    # after correctQuestion = 3, meaning the user has correctly answered their 3 recovery questions, go to catalogShopping() and user can start shopping
    catalogShopping()

'''
Because python is case sensitive, python recgonizes "Pencil" and "pencil" as different strings. The function converts masterCatalog list into all lowercase so that the keyword (item) will still pop up when searched for. 
'''
def searchByKeyword():
  # checking every element in the list 
  for i in range(0, len(masterCatalog)):
    # converting the first subelement (item name) in the first element into lowercase
    masterCatalog[i][0] = masterCatalog[i][0].lower()
    # converting the second subelement (item description) in the first element into lowercase
    masterCatalog[i][1] = masterCatalog[i][1].lower()

'''
Prompts the user to search for an item. Prompt the user enter their keywords into search. If the keyword is in the list, the program will append the item into searchedProducts = []. If the item does not exist a sorry message will be thrown and the user has the option to search again. After all products with the keyword are placed into searchedProducts = [], the program will call the sortRating function which sorts the list by greatest to least rating. The program will call the searchedProductsPrint function to manually print out the first 5 items in text onto the screen with their item numbers. 
'''
def searchingByProductOrDescription():
  # clearing searchedProduct list
  searchedProduct.clear()
  #converting the masterCatalogList into all lowercase
  searchByKeyword()
  # printing the header
  print("\n━━━━━━━━━━━━━━━━ 🔎 Searching... ━━━━━━━━━━━━━━━━")
  # asking user to search
  print("Please search below.")
  # prompting user to type in the search bar and converting text to lowercase and spliting the search into seperate words
  searchItemName = input("Search: ").lower().split(" ")
  # checking for each seperated word from searchItemName 
  for result in searchItemName:
    # for every item in masterCatalog
    for i in range(0, len(masterCatalog)):
      # if the word is in the item in masterCatalog item name or description 
      if result in masterCatalog[i][0] or result in masterCatalog[i][1]:
        #if the item that matches the keyword search is not already in the list (prevents items being double appended)
        if masterCatalog[i] not in searchedProduct:
          # add item to searchedProduct list
          searchedProduct.append(masterCatalog[i])
    # if the length of searcedProduct = [] is 0. This means no items in the masterCatalog list matches the user's search. 
  if len(searchedProduct) == 0: 
    # print out no item in masterCatalog list
    print("Sorry we do not sell this product.")
    # call function to being searching process again 
    searchingByProductOrDescription()
  # sort the products in searchedProduct = [] by rating 
  sortRating(searchedProduct)
  # sort the searchedProduct list by rating 
  searchedProductsPrint()
  # gives the user the option to sort by price, add to cart, or search for a different product
  priceSortChoice()

'''
Using bubble sorting, sortRating() sorts the searchedProduct list from Greatest to Least by Rating
'''
def sortRating(searchedProduct):
  # checks every item in the list
  for i in range(0, len(searchedProduct)):
    # checks every item in the sub list
    for j in range(0, len(searchedProduct) - 1):
      # checks if the first item in the list is less than or equal to the second item in the list
      if (searchedProduct[j][3] <= searchedProduct[j + 1][3]):
        # if the first item in the list is less than the second item, it will switch the order, so that the second item in the list is at the start of the list. 
        order = searchedProduct[j]
        searchedProduct[j] = searchedProduct[j + 1]
        searchedProduct[j + 1] = order

'''
Using bubble sorting, sortPrice() sorts the searchedProduct list from least to greatest by price
'''
def sortPrice(searchedProduct):
  # checks every item in the list
  for i in range(len(searchedProduct)):
    # checks every item in the sub list
    for j in range(0, len(searchedProduct) - 1):
      # checks if the first item in the list is less than or equal to the second item in the list
      if (searchedProduct[j][2] >= searchedProduct[j + 1][2]):
         # if the first item in the list is less than the second item, it will switch the order, so that the second item in the list is at the start of the list.
        order = searchedProduct[j]
        searchedProduct[j] = searchedProduct[j + 1]
        searchedProduct[j + 1] = order

'''
This product converts the searchedProduct List into text on the screen for the user. It displays the first 5 options from greatest to lowest rating. If there are less than 5 items that have the keyword, it will print all items. 
'''
def searchedProductsPrint():
  # printing the header
  print("\n━━━━━━━━━━━━━━━━ 🎨 Results Of Search ━━━━━━━━━━━━━━━━")
  # if the length of the searchedProduct list is less than or equal to 5 
  if len(searchedProduct) <= 5:
    # for every item in the list
    for i in range(len(searchedProduct)):
      # specifying the item number 
      print("Item Number - ", i + 1)
      # printing item name
      print("Name:", searchedProduct[i][0])
      # printing item description
      print("Description:", searchedProduct[i][1])
      # printing item price 
      print("Price: $", searchedProduct[i][2])
      # printing rating
      print("Rating:", searchedProduct[i][3], "/ 5\n" )
  # otherwise... the list of searchedProducts is more than 5 products
  else:
    # for every item in the list
    for i in range(5):
      # specifying the item number 
      print("Item Number - ", i + 1)
      # printing item name
      print("Name:", searchedProduct[i][0])
      # printing item description
      print("Description:", searchedProduct[i][1])
      # printing item price 
      print("Price: $", searchedProduct[i][2])
      # printing rating
      print("Rating:", searchedProduct[i][3], "/ 5\n" )

'''
Asks if the user would like to sort through the item they searched for by price (lowest to greatest). 1) If the user answers yes, the program will call the sortPrice() function, sort the items, and use the searchedProductsPrint() function to print the items onto the screen. 2) The user wants to add an item to cart. The program will call the addingToCart() function and the user can being to add items to their cart. 3) The user wants to search for an entirely different item. The program will call the catalogShopping() function and the user can search for a different item
'''
def priceSortChoice():
  # printing whether the person would like sort the searched items by price, add item to cart, or search for a different item
  print("Would you like to sort items by price, add item to cart, or search for a different item? \n1) Enter 1 to sort items by price\n2) Enter 2 to add item to cart\n3) Enter 3 to Search for a Different Product")
  # prompting user to answer question above 
  sortByPriceChoice = (int)(input("Answer: "))
  # if user inputs 1, this means the user would like to sort by price. 
  if sortByPriceChoice == 1:
    # call sortPrice function to sort the product by least to greatest price 
    sortPrice(searchedProduct)
    # calling searchedProductsPrint to manually print products on screen
    searchedProductsPrint()
    # start addingtoCart process by calling it's function 
    priceSortChoice()
  # if user inputs 2 they want to add an item to cart
  elif sortByPriceChoice == 2:
    # begin addingToCart process
    addingToCart()
  # if user inputs 3 they want to search for a different item
  elif sortByPriceChoice == 3:
    # user can being to search again
    catalogShopping()
  else:
    # print option not valid message
    print("\nThe option you selected is not valid. Please try again.")
    # loop the function and give them the choice to choose again
    priceSortChoice()

'''
Asks the user to pick an item on screen and quantity of the item they want. The items purchased is appended into shoppingCart = [] and the quantity is appended to quantityOfItemsPurchased = []. When items are added, a successfully added message will be printed. The program will then ask the user if they want to continue shopping or checkout by calling the checkoutOrContinueShopping() function
'''
def addingToCart():
  # printing adding to cart process instructions
  print("\nEnter the item number and quantity to add to cart.")
  # prompt user to enter item number they want to purchase
  buyItemNumber = (int)(input("Item Number: "))
  # prompt user to enter the quantity of that product
  quantityOfItem = (int)(input("Quantity: "))
  # adding the user input quantity of products purchased to quantityOfItemsPurchased list
  quantityOfItemsPurchased.append(quantityOfItem)
  # adding the user input product purcchased to shoppingCart list
  shoppingCart.append(searchedProduct[buyItemNumber - 1])
  # printing successfully added to cart message
  print("\n🛒 Successfully Added to Cart!")
  # prompting user if they would like to checkout or continue shopping by calling checkoutOrContinueShopping function
  checkoutOrContinueShopping()

'''
Asks the user if they want to continue shopping or proceed to checkout. If the user chooses to continue shopping, the program will return the catalogShopping() function and allow the user to search for a new product. If the user chooses to checkout, the program will return the receipt() function. Otherwise, if the user inputs an invalid answer, they will be asked again whether they want to shop or checkout by looping the function. 
'''
def checkoutOrContinueShopping():
  # printing instructions to checkout or continue shopping
  print("\nWould you like to continue shopping, checkout, or search ?\n1) Enter 1 to Continue Shopping\n2) Enter 2 to proceed to Checkout")
  # prompting the user to input their answer
  checkoutOrShop = (int)(input("Answer: "))
  # if the user chooses 1, call the catalogShopping() function
  if checkoutOrShop == 1:
    catalogShopping() 
  # if the user chooses 2, call the receipt() function
  elif checkoutOrShop == 2:
    receipt()
  # otherwise, if the user does not enter a valid option, the program will loop and ask the user if they want to checkout or continue shopping
  else:
    print("That is not a valid option. Please pick again.")
    checkoutOrContinueShopping()

'''
Prompt the user for their payment method. Prompt the user if their billing and shipping address is the same. If the shipping and billing address is the same, the program will only ask for one address. If the shipping and biling address is not the same, the program will ask for seperate addresses. If the user chooses an invalid option, the program will ask what their payment method and shipping/billing address is again. For every item in the shopping cart index 2, we multiply by the quantity in quantityOfItemsPurchased list to find each individual total of 
'''
def receipt():
  #declaring shippingAddress as an empty space
  shippingAddress = ""
  # printing checkout header
  print("\n━━━━━━━━━━━━━━━━ 🛒 Checkout ━━━━━━━━━━━━━━━━")
  # Giving user intstructions on how to pay
  print("How would you like to pay?\n1 ✧ MasterCard\t\t2 ✧ Debit Card\n3 ✧ Cat's Gift Card\t4 ✧ Credit Card\n")
  # prompting the user to enter their payment method
  paymentMethod = (input("Please enter number associated with the payment method: "))
  # checks if paymentMethod = 1
  if paymentMethod == "1":
    # declare paymentMethod as mastercard
    paymentMethod = "MasterCard"
  # checks if paymentMethod = 2
  elif paymentMethod == "2":
    # declare paymentMethod as debit card
    paymentMethod = "Debit Card"
  # checks if paymentMethod = 3
  elif paymentMethod == "3":
    # decalre paymentMethod as cat's gift card
    paymentMethod = "Cat's Gift Card"
  # checks if paymentMethod = 4
  elif paymentMethod == "4":
    # decalre paymentMethod as credit card
    paymentMethod = "Credit Card"
  # otherwise.. the user has not entered a valdi option
  else:
    # print wrong option message
    print("That is not a valid option.")
    # start function again to ask user for correct paymentMethod
    receipt()
  # asking user if their billing address is the same as their shipping address
  print("\nIs your billing address the same as your shipping address?\n1) Enter 1 for Yes\n2) Enter 2 for No")
  # prompting user to answer 1 or 2 
  isAddressSame = (int)(input("Option: "))
  # if the user enters 1, it means their billing and shipping address is the same
  if isAddressSame == 1: 
    # prompt user to enter an address
    billingAddress = input("Please input your address: ") 
    # creating the shippingAddress by adding the billing address to the shippingAdress variable
    shippingAddress = shippingAddress + billingAddress
  # if the user enters 2, it means their billing address and shipping address is different
  elif isAddressSame == 2:
    # prompt user to enter their billing adress
    billingAddress = input("Billing Address: ")
    # prompt user to enter their shipping adress
    shippingAddress = input("Shipping Address: ")
  # otherwise the user has not entered a valid option
  else:
    # print not valid message
    print("Option not valid.")
    # call receipt() function to have user enter their payment method and addresses
    receipt()
  # printing receipt header
  print("\n━━━━━━━━━━━━━━━━ 🧾 Receipt ━━━━━━━━━━━━━━━━\n")
  # declaring subtotal variable as 0 
  subtotal = 0 
  # for every item in the shopping cart
  for i in range(0, len(shoppingCart)):
    # subtotal = subtotal + item name price * quantity of items purchased
    subtotal = subtotal + (shoppingCart[i][2] * quantityOfItemsPurchased[i])
    # printing item number
    print("Item", i + 1)
    # printing item quantity
    print("Quantity:", quantityOfItemsPurchased[i])
    # printing the item total 
    print("Item Total: $", round(shoppingCart[i][2] * quantityOfItemsPurchased[i], 2))
    print("Name:", shoppingCart[i][0])
    # printing item description
    print("Description:", shoppingCart[i][1])
    # printing item price 
    print("Unit Price: $", shoppingCart[i][2])
    # printing rating
    print("Rating:", shoppingCart[i][3], "/ 5\n" )
    print("")
  # taking the subtotal and rounding to 2 decimal places
  roundedSubtotal = round(subtotal, 2)
  # find 0.13 of subtotal and roudning to 2 decimal places
  tax = round(subtotal * 0.13, 2)
  # finding the total by adding the tax and subtotal
  total = subtotal + tax
  # printing payment method 
  print("Payment Method:", paymentMethod)
  # printing billing address
  print("Billing Address:", billingAddress)
  # printing shipping address
  print("Shipping Address:", shippingAddress, "\n")
  # printing subtotal
  print("Subtotal: $",roundedSubtotal)
  # printing tax
  print("Tax: $", tax)
  # printing final total
  print("Total: $", round(total,2), "\n")
  # printing farewell message
  print("✧･ﾟ: *✧･ﾟ:* 🎨 Thank you for shopping at Cat's Art Store! *:･ﾟ✧*:･ﾟ✧")

'''
Prints all items avaliable for sale and prompts user to start searching. After the user searches, they have the option to sort their search results by price.
'''
def catalogShopping():
  # printing header
  print("\n━━━━━━━━━━━━━━━━ 🎨 Catalog of Cat's Art Store ━━━━━━━━━━━━━━━━")
  # printing items for sale
  print("Welcome to our store catalog! Here you can find many different art supplies. Our store sells:\n✧ Drawing Kit\t\t✧ Acrylic Paint\n✧ Colouring Book\t✧ Watercolour\n✧ Canvas\t\t\t✧ Markers\n✧ Fountain Pen\t\t✧ Paint Brushes\n✧ Erasers\t\t\t✧ Pencils")
  # calling search function
  searchingByProductOrDescription()

'''
Main function that holds all other functions. 
'''
def main():
  # welcome screen
  welcomeScreen()

# calling main function to start program
main()



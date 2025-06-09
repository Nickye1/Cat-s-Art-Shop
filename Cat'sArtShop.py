# import random to use python function random.choice() to randomize resetPasswordQuestions during account creation 
import random
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
masterCatalog = [["Arteza - 140-PCS Wooden Drawing Kit", "Includes 60 Crayons, 60 watercolour pans, 10 paintbrushes, 10 HB pencils", 40.99, 5], ["Ohuhu Signature Mixed Media Drawing Kit, 200 PCS", "Includes 50 Papers, 10 Pencils, 100 Markers, 30 Watercolour pans, 10 Brushes",	70.99, 4.4], ["74PCS Drawing Kit Set - Pro Art Supplies", "Includes Sketchbook, Watercolor Paper, Watercolor, Graphite, Metallic, Pastel", 74.00,	4.5,],["Drawing Kit Pencils and Sketch Set Professional 57 Pieces",	"Drawing and Sketching Pencil Set with Portable Case Sketch Pencils", 75.50,	2.8],["54 Pack Teen Kids Beginners, Adult Art Supplies Drawing Kit", "Artist Drawing Supplies, Colored Pencils, Sketch Kit, Sketchbook 50 Pages", 95.00, 3.1],["78-Piece Pencils Drawing Kit", "Drawing Sketching Pencils Set with Sketchbook, Coloring Book, Sketching Pencils", 110.00, 4.1],["Complete Drawing Kit with Sketchbook", "8 Drawing Pencils, 3 Charcoal Pencils, 1 Graphite Pencil, 2 Charcoal Sticks",	79.99, 2.7],["Merooart 54-Pack Adult Art Kit", "Drawing Pencil Set Zipper Box: Sketch Books, Coloring Books, Watercolor Pens", 89.00, 2.2],["Art 101 Doodle and Color 142 Pc Art Kit", "Includes 24 Premium Colored Pencils, crayons, oil pastels, watercolors", 100.00, 3.5],["239PC Art Kit for Kids", "Sketch Book, KINSPORY Coloring Art Kit, Markers, Crayon, Colour Pencils", 159.99, 3.3],["Arteza Acrylic Paint 20-PCS", "Easy-to-Use Acrylic Paints - 20 Colours", 19.99, 4.5], ["Ohuhu Craft Acrylic Paint 24-PCS",	"Craft Acrylic Paint, Set of 24 Colours (2 oz/Bottle), Water-Based, Non Toxic", 30.99,	2.2],["Mont Marte Acrylic Paint Set 24 Colours", "Acrylic Paint Set 24 Colours 36ml, Perfect on Canvas",	45.99,	3.1],["Blick Acrylic Paint Set 26 Colours", "Acrylic Paint Set, 36 x 36ml Tubes, Semi-Matte Finish", 50.00, 4.7],["Windsor Newton 10-PCS Acrylic Paint Set",	"High quality Acrylic which delivers professional results - 60 ml (Pack of 10)", 60.99,	5],["Arctechno 15 Colours Acrylic Paint Colours", "Acrylic Paint Set Contains 15 Bright Colors (12ml/tube 0.4oz)", 35.00, 3.3],["Abeier Set of 24 Metallic Colors", "Value Set for Starters or Adult Artists | Premium Quality (2oz/60ml Bottle)",	27.99,	2.1], ["LiuLiuCai 24 Colors Acrylic Paint Set", "Includes 12x Brushes & Palette Non-Toxic & Vibrant Colours (12ml/tube 0.4oz)", 25.99,	2.3],["Pikachu Set of 50 Acrylic Paint Set", "Pikachu Themed Acrylic Paint Set 50 Colours 36ml, Perfect on Canvas",	26.00,	3.4],["MeowMeow 20 Colors Acrylic Paint Set", "Virbant Colours (30ml/tube 0.4oz) Perfect for Beginner Artists", 25.50,	2],["Arteza - Dinosaur Colouring Book", "Includes 60 pages of colouring (8.3 x 11.7 inches)", 15.50,	3.3], ["Nintendo - Pokemon Colouring Book",	"First Generation Pokemons includes 350 pages of colouring (8.3 x 11.7 inches)", 25.99,	5], ["Nintendo - Animal Crossing Colouring Book", "Animal Crossing New Horizons Villagers Colouring Book includes 100 pages", 35.99,	4.1],["Indigo - Adult Flower Colouring Book", "Perfect for Adults | Colour flowers includes 200 pages made of recycled paper",	15.99,	3.3],["Animals Colouring Book: Perfectly Portable Pages", "Printed on one side only of archival-grade, acid-free, 200-year paper",	13.99, 4.5],["Disney Princess Colouring Book", "Includes all Disney Princesses, made with recycled paper, includes 150 pages", 14.99, 3.2], ["Ohuhu - Under the Sea Colouring Book","Includes Sharks, Fish, Mermaids, Jellyfish, and other Marine Organisms",	30.99,	2.2], ["Spongebob Colouring Book", "Includes all Spongebob settings includes 50 pages and stickers!", 15.00, 2.3],["Avatar the Last Airbender Colouring Book",	"Features the 4 elements and main characters made of recycled paper - 20 pages", 10.99, 4.8],["Vegtables Colouring Book", "Learn your vegtables and colour! 30 pages Virbant line art for colouring",	5.00, 3],["Arteza Watercolour Painting Kit", "24 Premium Quality Art Watercolours Painting Kit (12 ml, 0.42 oz.) with 6 Brushes",	20.99, 4.5],["Blick Art Studio Watercolour Painting Kit", "30 Vibrant Colours Art Watercolors Painting Kit, Paper Pad Versatile",	25.99,	2.2],["ARTISTRO Watercolour Paint Set", "48 Vivid Colours in Portable Box, Including Metallic and Fluorescent Colors", 26.00,	3.1],["Paul Rubens Watercolour Paint Set", "24 Muted Colours Highly Pigmented, 5ml Watercolor Paint Tubes", 15.99, 4.7],["Artists Watercolour Paint Set", "36 Colours Advanced Vivid Water Colors Paint Art Kit", 13.99,	2.1],["Winsor & Newton Cotman Watercolour Paint Set",	"Contains 10 essential starter colors, formulated for high transparency", 60.99, 2.3],["HIMI Solid Watercolour Paint Set", "Durable and will not Easy Crack (24 Vivid Colors)", 35.00,	3.4],["Komorebi Japanese Watercolour Paint Set", "40 Colors - Including Metallic and Neon - Artist Quality - Richly Pigmented",	40.99,	2],["Mont Marte Watercolour Paint Set",	"36 Vibrant Colours with 1 Paint Brush, Ideal for Watercolour Painting", 25.50, 4.3],["Crayola Watercolour Paint Kit", "20 Premium Quality Art Watercolours - Pigmented - Active - (12 ml, 0.42 oz.)",	23.00,	3],["Arteza 15 Blank Canvas", "(5 x 7in) Blank White Canvas Panels, 100% Cotton, 8 oz Gesso-Primed", 25.00, 5],["Painting Canvas Panels, Ohuhu",	"20 Pack 8x10 Inch Canvas Boards Canvases 100% Cotton, Primed Canvas Panel", 20.99, 4.7],["FIXSMITH Painting Canvas Panels", "12x16 inch Professional Quality Canvas Painter Paper Boards, Super Value 12 Pack",	35.00, 2.3],["Blank Painting Canvas Panel, White Canvas Board (Hexagonal)", "6PCS/Set Artist Cotton Stretched Primed Decoration Boards", 50.00, 3.1],["FIXSMITH Stretched White Blank Canvas", "8x10 Inch, Bulk Pack of 12, Primed, 100% Cotton, 5/8 Inch Profile of Super Value",	19.99, 2.6],["12 Packs Blank Art Canvas Panels", "8in x10in (20cm x 25cm) Pre Stretched Canvas Board Artist Painting Stretcher", 30.99, 2.2], ["QLOUNI 24 Pack Mini Stretched Canvas", "4x4 Inch, 3/10 Profile Art Primed Canvases for Painting, 100% Cotton", 25.50, 3.5],["CONDA Primed Canvas 8 Pack", "8x10 inch Stretched Canvas, Pack of 10, White Blank Canvas, 100% Cotton", 50.00, 4.1], ["9 Pieces Canvas Panels Artist Blank Canvas", "Assorted Size Art Canvas Multi Panel Canvas Boards Creative Blank Painting",	60.99, 3.2],["5 Packs Blank Canvas Panels Board", "30 x 40 cm(12 x 16), 100% Cotton for Acrylic Painting", 60.99, 4.4],["Crayola Super Tips Washable Markers 100 Count Arts & Crafts",	"Washable colours from clothing, most household furniture, and skin!", 25.00, 5],["Alcohol Markers Dual Tips Permanent Art Markers", "For Kids & Adult, Alcohol-Based Highlighter Pen Sketch Markers for Painting", 20.99, 4.1],["Coloring Markers Pen for Adults Kids",	"36 Fine Felt Tip Water Markers Dual Brush Pens for Students", 35.00, 4.5],["Crayola 58-4324 24 Pip-Squeaks Skinnies Markers", "Fine Line Washable Markers, School and Craft Supplies, Ages 3, 4, 5, 6", 15.00, 2.2],["100 Colors Art Markers for Adult Coloring", "Ohuhu Dual Tips Art Brush Marker Fineliner Color Marker Pens", 10.99, 2.1],["48 Colors Dual Brush Art Markers", "Alcohol Based Marker with Carrying Case Dual Tip for Coloring/Illustration AT04", 50.00, 3.8],["168 Colors Alcohol Markers Art Markers for Drawing Professional", "Dual Tips markers Permanent marker for Adults & Kids (168 black)", 30.99, 4.8],["Ohuhu 60 Watercolor Art Markers Dual Tips", "Brush Fineliner Coloring Color Pens, Water Based Marker for Calligraphy",	13.99, 2.2], ["Super Squiggles Markers - 12 Colors Self Outline Markers", "Double Line Pen, Outline Markers Pens for Art", 60.99, 5],["Posca Full Set of 8 Acrylic Paint Markers", "Pens with Reversible Medium Point Pen Tips, Posca Pens are Acrylic Paint Markers", 15.99, 4.3],["Wordsworth & Black Fountain Pen Set, Medium Nib", "Includes 6 Ink Cartridges and Ink Refill Converter Pens [Silver Gold]",	25.00, 5],["Scriveiner British Racing Green Fountain Pen", "Stunning Luxury Pen with Chrome Finish, Schmidt Nib (Medium)", 20.99, 4.4],["MUJI Aluminum Fountain Pen",	"Made in Japan ink colour black made Aluminum (5 pack)",	35.00, 4.5],["Waterman Allure Fountain Pen", "Mint Green Matte Lacquer with Chrome Trim | Fine Stainless Steel Nib | Blue Ink",	15.00, 2.2],["Parker Sonnet Fountain Pen", "Black Lacquer with Gold Trim, Medium Nib (1931495)", 30.00, 2.2],["Hethrone Quill Fountain Pen and Ink Set",	"5 pens, 1 non-toxic colorful ink, 1 seal, 1 letter opener and 5+12 replaceable nibs",	19.99, 3.3],["Wordsworth & Black's Fountain Pen Set", "Medium Nib, Gift Case; Includes 6 Ink Cartridges, Ink Refill Converter",	30.99, 4.5],["Abcsea Vintage Style Fountain Pen Silver Clip",	"stainless steel nib, advanced liquid ink system and unique real fountain pen", 40.99, 2.1],["JINHAO X450 Fountain Pen (Green Marble, Medium Nib 0.7mm)",	"Nib: M (steel nib), Cap: push type; Converter: screw type",	25.50, 5],["HongDian 920 Black Metal Fountain Pen, Rose Gold Plated", "converter for bottled ink, Ink cartridges ASIN: B08259HPC7", 23.00, 4.5],["UPINS 30 Pcs Paint Brushes Small Brush Bulk for Detail Painting",	"ARTECHO Paint Brush Set for Watercolor, Acrylic, Oil, Gouache",	15.99, 4.4],["BOSOBO Paint Brushes Set","2 Pack 20 Pcs Round Pointed Tip Paintbrushes Nylon Hair Artist Brushes", 18.99,	4.5],["Crayola 05-3506 5 Assorted Premium Paint Brushes",	"School, Craft, Painting and Art Supplies, Kids, Ages 3,4, 5, 6 and Up", 14.99, 2.2],["Artist Paint Brush Set-15pcs Professional Paint Brushes", "Acrylic Painting Watercolor Oil Gouache for Artists Include Pop-Up Carrying Case", 30.99, 3.3],["Artecho Art Paint Brushes 20pcs", "Set for Watercolor, Acrylic, Oil", 15.00, 4.5],["AIEX 12Pcs Paint Brushes",	"Anti-Shedding Nylon Hair Flat Shader Tip Artist Paintbrushes", 22.00, 3.2],["Miniature Paint Brushes 15", "Detail Paint Brushes with Fine Tips Ergonomic Handles Dagger Brush", 14.99, 1.5],["Crafts 4 All Acrylic Paint Brushes", "Professional, Nylon Watercolor Brushes - Set of 12 Painting Supplies Set",	30.99, 2.3],["Mokani 5PCS Paint Brushes",	"Nice Bristle Paintbrush Heads, Stain Brushes for Woodwork", 17.99,	4.8],["KINBOM 6PCS Detail Paint Brush Set",	"Miniature Paint Brushes Thin Detail Paint Brush Paint Brush Fine Paint Brushes", 25.00, 3],["EULANT Pencil Erasers 9 Pieces", "White 2B Rubbers Erasers for Universal Use in Schools Office Sketching", 5.99, 4.4],["Pentel Hi-Polymer Large Erasers 2-Pack, White - ZEH10BP-2",	"High quality rubber eraser removes lead easily and cleanly", 7.99, 4.5],["Faber-Castell Erasers - Drawing Art kneaded Erasers - 4 Pack", "Art Eraser Kneaded : Sold in Pack of 4 Kneaded Eraser pack - Grey Color", 11.50, 2.2],["ONTYZZ 9 Pack Erasers", "Storage Box Large White Erasers for School Office Art Erasers", 3.40, 3.3],["150 Pieces Mini Erasers for Kids Bulk",	"150 Pieces Mini Erasers for Kids Bulk, Novelty Animal Erasers, Pencil Erasers", 10.99, 4.5],["40-Piece Eraser, Plastic Eraser", "White Plastic Eraser, 2B Eraser, Suitable for School, Sketching, Painting, Visual Arts",	6.70, 2.2],["PRISMACOLOR DESIGN Eraser, Multi-Pack Erasers", "Made with rubber Use for erasing graphite, charcoal, pastel and crayon", 15.99, 3.1],["KLEBREIS Cute Pencil Erasers", "12Pcs Cartoon Animal Themed Rubber Erasers Roller Colorful Rectangle Eraser", 2.99, 4.7],["Dixon 70102S White Vinyl Block Erasers 2 Large + 2 Bonus Small", "No messy residue - Leaves clear, smudge-free surfaces, Works on paper",4.50, 2.1],["Paper Mate SPEED Erasers 2-Carded, White (70823)", "PAPER MATE White Rectangular Pieces 2", 1.99, 4.5],["AmazonBasics Pre-sharpened Wood Cased #2 HB Pencils, 30PC",	"Strong medium-soft lead produces long-lasting, smooth, readable strokes",	2.99, 4.7],["Staedtler Norica 50 Graphite HB2 Pencils + 50 eraser caps", "Presharpened graphite pencils includes 50 Latex and PVC free eraser tips", 4.50, 2.1],["Dixon Ticonderoga Primary Pencils, 2, Yellow, Box of 12 (13308)", "Dixon Ticonderoga graphite pencils",	1.99, 2.3], ["BIC Matic Grip Mechanical Pencils, Black, 0.7mm, 5-pack",	"Rubber grips to make writing comfortable Top advance mechanical pencil", 3.50, 3.4],["MozArt Mechanical Pencils Set with Case - 4 Sizes",	"0.3, 0.5, 0.7 & 0.9mm with 30 HB Lead Refills Each & 4 Eraser Refills",	10.99, 2.2],["Pencil Buddies Pro Graphite Drawing Pencils Set - 8B-6H",	"12 Sketching Art Pencils for Sketch Art and Shading", 7.00, 3.3],["Bostitch Office Premium #2 Pencils", "American Cedar Wood, Pre-Sharpened, HB Graphite, 24-Pack Smudge resistant",	15.99, 4.5],["BIC Extra-Sparkle Mechanical Lead Pencils Medium Point 0.7 mm", "24-Count (Pack of 1), Refillable Design for Long-Lasting Use, Blue, Green, Orange", 12.00, 2.2], ["Paper Mate Pencils, Classic Wood Pencil # 2, Box of 12",	"Pencils HB #2, 12 Pcs/Box, Rubber Tipped Graphite Pencils, Wood Pencils", 6.70, 3.1], ["Dixon Oriole No:2 Pre-Sharpened Pencils",	"Made from fine quality woods from sustained yield forests box of 12 yellow pencil",	15.99, 4.7]]

# Stores all products that match the search keyword into the list

shoppingCart = []
quantityOfItemsPurchased = []

'''
Creating the Welcome Screen to the website. Displays password requirements needed to create an account. 
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
    for i in range(0, 3):
      # storing the random question from resetPasswordQuestions = [] into a variable
      question = random.choice(resetPasswordQuestions)
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
Prompting user to login using the created username and password. If the login information is correct they can be start shopping. Otherwise, if the login information is incorrect after 3 tries, the recovery questions will be printed and the program will prompt the user for the answers. If the answers do not match with the answer they gave during account creation, it will repeatedly ask the same question until they answer correctly. 
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
      # comparing the answer entered during account creation to answer during recovery question. If the answer is the not the same, print wrong answer message. 
      elif askedResetQuestionAnswer != resetPasswordAnswers[correctQuestion]:
        print("Your answer is wrong. Try again.")
    # after correctQuestion = 3, meaning the user has correctly answered their 3 recovery questions, go to catalogShopping() and user can start shopping
    catalogShopping()

'''
Because python is case sensitive, python recgonizes "Pencil" and "pencil" as different strings. The function converts masterCatalog list into all lowercase so that the keyword (item) will still pop up when searched for. 
'''
def searchByKeyword():
  # checking every element in the list 
  for i in range(0, len(masterCatalog)):
    # checking every element in every sublist 
    for j in range(0, len(masterCatalog[i])):
      # converting the first subelement (item name) in the first element into lowercase
      masterCatalog[i][0] = masterCatalog[i][0].lower()
      # converting the second subelement (item description) in the first element into lowercase
      masterCatalog[i][1] = masterCatalog[i][1].lower()

'''
Prompts the user to either search by product description or product name. Prompt the user enter their keywords into search. If the keyword is in the list, the program will append the item into searchedProducts = []. If the item does not exist a sorry message will be thrown and the user has the option to search again. After all products with the keyword are placed into searchedProducts = [], the program will call the sortRating function which sorts the list by greatest to least rating. The program will call the searchedProductsPrint function to manually print out the first 5 items in text onto the screen with their item numbers. 
'''
searchedProduct = []

def searchingByProductOrDescription():
  searchedProduct.clear()
  #converting the masterCatalogList into all lowercase
  searchByKeyword()
  # printing the header
  print("\n━━━━━━━━━━━━━━━━ 🔎 Searching... ━━━━━━━━━━━━━━━━")
  # asking user if they would like to search by product name or description
  print("Would you like to search by product or description?\n1) Enter 1 for Item Name\n2) Enter 2 for Description")
  # prompting user to enter their choice
  productDescriptionInput = (int)(input("Enter: ")) 
  # if the user inputs 1, they want to search by item name 
  if productDescriptionInput == 1: 
    # printing instructions
    print("You are searching by item name.")
    # prompting user to type in the search bar 
    searchItemName = input("Search: ")
    # coverting the user's searchItemName input into lowercase to be regonized in the masterCatalogList
    searchItemName = searchItemName.lower()
    # checking every item in the list 
    for i in range(len(masterCatalog)):
      # checking if the item name in the list matches the user's searches
      if searchItemName in masterCatalog[i][0]:
        # if there is a keyword and item name match, the item is appended to the searchedProduct = []
          searchedProduct.append(masterCatalog[i])
    # if the length of searcedProduct = [] is 0. This means no items in the masterCatalog list matches the user's search. 
    if len(searchedProduct) == 0: 
      # print out no item in masterCatalog list
      print("Sorry we do not sell this product.")
      # call function to being searching process again 
      searchingByProductOrDescription()
    # sort the searchedProduct list by rating 
    sortRating(searchedProduct)
    # call searchedProductsPrint() to manually print the items onto the screen with their item numbers 
    searchedProductsPrint()
  # if the user inputs 2, this means they want to search by item description.
  elif productDescriptionInput == 2:
    # printing instructions
    print("You are searching by product description.")
    # prompting user to type in the search bar 
    searchItemName = input("Search: ")
    # coverting the user's searchItemName input into lowercase to be regonized in the masterCatalogList
    searchItemName = searchItemName.lower()
    # checking every item in the list 
    for i in range(len(masterCatalog)):
       # checking if the item description in the list matches the user's searches
      if searchItemName in masterCatalog[i][1]:
        # if there is a keyword and item description match, the item is appended to the searchedProduct = []
          searchedProduct.append(masterCatalog[i])
    if len(searchedProduct) == 0: 
      # print out no item in masterCatalog list
      print("Sorry we do not sell this product.")
       # call searchedProductsPrint() to manually print the items onto the screen with their item numbers 
      searchingByProductOrDescription()
    # sort the products in searchedProduct = [] by rating 
    sortRating(searchedProduct)
    # manually print them on screen 
    searchedProductsPrint()

'''
Using bubble sorting, sortRating() sorts the searchedProduct list from Greatest to Least by Rating
'''
def sortRating(searchedProduct):
  # checks every item in the list
  for i in range(0, len(searchedProduct)):
    # checks every item in the sub list
    for j in range(0, len(searchedProduct) - 1 - i):
      # checks if the first item in the list is less than the second item in the list
      if (searchedProduct[j][3] < searchedProduct[j + 1][3]):
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
    for j in range(0, len(searchedProduct) - 1 - i):
      # checks if the first item in the list is less than the second item in the list
      if (searchedProduct[j][2] > searchedProduct[j + 1][2]):
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
      print("Item Number", i + 1)
      # for every sub item in the list
      for j in range(0, len(searchedProduct[i])):
        # print the sub item in the sublist
        print(searchedProduct[i][j])
      # after each item is printed, print a space to seperate 
      print("")
  # otherwise... the list of searchedProducts is more than 5 products
  else:
    # for every item in the list
    for i in range(5):
      # specifying the item number
      print("Item Number", i + 1)
      # for every sub item in the list
      for j in range(0, len(searchedProduct[i])):
        # print the sub item in the sublist
        print(searchedProduct[i][j])
      # after each item is printed, print a space to seperate 
      print("")

'''
Asks if the user would like to sort through the 5 items on screen after searching by price (lowest to greatest). 1) If the user answers yes, the program will call the sortPrice() function, sort the items, and use the searchedProductsPrint() function to print the items onto the screen. The program will then direct the user to adding an item to the cart. 2) If the user answers no, the program will direct the user to adding an item to the cart.
'''
def priceSortChoice():
  # printing whether the person would like sort the searched items by price 
  print("Would you like to sort by price?\n1) Enter 1 for Yes\n2) Enter 2 for No")
  # prompting user to answer question above 
  sortByPriceChoice = (int)(input("Answer: "))
  # if user inputs 1, this means the user would like to sort by price. 
  if sortByPriceChoice == 1:
    # call sortPrice function to sort the product by least to greatest price 
    sortPrice(searchedProduct)
    # calling searchedProductsPrint to manually print products on screen
    searchedProductsPrint()
    # start addingtoCart process by calling it's function 
    addingToCart()
  # if user inputs 2
  elif sortByPriceChoice == 2:
    addingToCart()
  # if user inputs any other value besides 1 or 2
  else:
    # print option not valid message
    print("\nThe option you selected is not valid. Please try again.")
    # loop the function and give them the choice to choose again
    priceSortChoice()

'''
Asks the user to pick an item on screen and quantity of the item they want. The items purchased is appended into shoppingCart = [] and the quantity is appended to quantityOfItemsPurchased = []. When items are added, a successfully added message will be printed. The program 
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
  print("\nWould you like to continue shopping or checkout?\n1) Enter 1 to Continue Shopping\n2) Enter 2 to proceed to Checkout")
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
  print("How would you like to pay?\n✧ MasterCard\t\t✧ Debit Card\n✧ Cat's Gift Card\t✧ Credit Card\n")
  # prompting the user to enter their payment method
  paymentMethod = input("Payment Method: ")
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
    print("Item Total: $", shoppingCart[i][2] * quantityOfItemsPurchased[i])
    # for every sublist element
    for j in range(0, len(shoppingCart[i])):
      # print each elemetn in a sublist
      print(shoppingCart[i][j])
    # print a space after each item
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
  # calling priceSortChoice() to give user option to sort their results by price
  priceSortChoice()

'''
Main function that holds all other functions. 
'''
def main():
  # welcome screen
  welcomeScreen()

# calling main function to start program
main()

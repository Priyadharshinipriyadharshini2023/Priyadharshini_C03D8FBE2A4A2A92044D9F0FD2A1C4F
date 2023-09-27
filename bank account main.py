'''Implement a class called Player that represents a cricket player. The Player class should have a
method called play() which prints "The player is playing cricket. Derive two classes, Batsman and
Bowler, from the Player class. Override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each object.'''


# Define the base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()￼Not
[20/09, 2:05 pm] +91 79041 88790: class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:  
      self.__account_balance += amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid deposit amount.")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -=amount
      print("withdraw ₹{}. New balance: ₹{}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid withdraw amount or insufficient balance : ")
  def display_balance(self):
    print("Account balance for {} (Account #{}: ₹{}".format(
        self.__account_holder_name,self.__account_number,
        self.__account_balance))
account = BankAccount(account_number="9042442317",
                      account_holder_name="PRABHAKRAN",
                      initial_balance=10000.0)
account.display_balance()
account.deposit(5000.0)
account.withdraw(2000.0)
account.withdraw(20000.0)
account.display_balance()
[20/09, 2:05 pm] +91 79041 88790: class player:
    def play(self):
      print(" THE PLAYER IS PLAYING CRICKET .")
class Batsman(player):
    def play(self):
        print(" THE BATS MAN IS BATTING. ")
class Bowler(player):
    def paly(self):
        print(" THE BOWLER IS BOWLING. ")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()

# Exercise: Set intersections
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend

# Add the name to the empty set

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
name = input("Enter the name of the user: ")
user_friends.add(name)
friends_nearby = user_friends.intersection(nearby_people)
print(friends_nearby)

#-------------------------------------------------------------------------------------

# Exercise: Dictionary
lottery_numbers = {12,21,23,5,8}

#creation of player profile (Dictionry inside a list)
players=[
  {
    'name':'Pavan Kumar',
    'numbers': {1,4,6,8,10}
  },
  {
    'name': 'Guangli',
    'numbers': {12,5,8,29,31}
  }
]

print(players[0]['name'])
right_numbers_pavan = lottery_numbers.intersection(players[0]['numbers'])
print(right_numbers_pavan)

right_numbers_guangli = lottery_numbers.intersection(players[1]['numbers'])
print(len(right_numbers_guangli))

print("Player "+players[0]['name']+" got "+str(len(right_numbers_pavan))+" right")

print("Player "+players[1]['name']+" got "+str(len(right_numbers_guangli))+" right")

#---------------------------------------------------------------------------------------

# Exercise: A simple text Menu 
#p = True
user_input = input("Enter either p/q: ")
if(user_input == 'p'):
  print("Hello")
while (user_input=='p'):
  #print("Hello")
  user_input = input("Enter either p/q:")
  if (user_input=='p'):
    print("Hello")
  else:
    exit
#-----------------------------------------------------------------------------------------
  
# Exercise: FizzBuzz
# Between Numbers 1 to 10 (inclusive)
'''
for i in range(1,101):
  if (i%3 is 0) and (i%5 != 0):
   print(f'Fizz')
  elif (i%5 is 0) and (i%3 !=0):
    print(f'Buzz')
  elif (i%3 is 0) and (i%5 is 0):
    print(f'FizzBuzz')
  else:
    print(f'{i}')
'''
    #-------------------------------------------------------------------------------
# Exercise: An Improved lottery 
import random

# Creating a set of 6 ranndom numbers
lottery = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
best_player_score = []
for player in players:
  #print(player['numbers'])
  num_match = len(player['numbers'].intersection(lottery))
  num_match_score = 100 ** num_match
  # Now make a dict of name and score
  tuple_maker = (player['name'],num_match_score)
  #print(tuple_maker)
  best_player_score += tuple_maker
  # print(f'{player["name"]} won {num_match_score}')

# zipping an otherwise list into tuple
#print(best_player_score)
zipped_tuple = dict(zip(best_player_score[::2], best_player_score[1::2]))

#print(zipped_tuple)
Maax_winner = [(value, key) for key, value in zipped_tuple.items()]
print (f'{max(Maax_winner)[1]} won {max(Maax_winner)[0]}' )

#print(max(win_dict.items()))

# -------------------------------------------------------------

# simple max Finder
lister = [1, 3, 67, 5, 32, 4] 
temp = 0
for num in lister:
  if num > temp:
    temp = num
  else:
    continue
print (temp)

# ------------------ Magic Methods in Python ------------
class Club:
  def __init__(self,name):
    self.name = name
    self.players = []
  def __len__(self):
    return len(self.players)  
  def __getitem__(self, item):
    return self.players[item]
  def __repr__(self):
    return f'Club {self.name}: ["{self.players[0]}","{self.players[1]}"]'
  def __str__(self):
    return f'Club {self.name} with {Club.__len__(self)} players'
  
club = Club('Arsenal')
print(f'{club.name}')
club.players.append('Rolf')
club.players.append('Anne')
print(f'Number of club members: {len(club)}')
print(f'Club Member: {club[0]}')
print(club)

# list of dictionaries
books = []
books.append(
  {'name': 'Pavan',
  'age': 25,
  'gender': 'M'
  })

books.append( {
    'name': 'Nivedha',
    'age': 25,
    'gender': 'F'
  })
books.append({
    'name': 'Manvitha',
    'age': 25,
    'gender': 'Unknown'
  }
)
'''
# Naive way to accomplish deletion of an entry
for ite in books:
  if ite['name'] == 'Manvitha':
    books.remove(ite)

print(f'{books}')
'''

# Professional way to do it 
books1 =[]
for book in books:
  if book['name'] != 'Pavan':
    books1.append(book)
  else:
    continue
print(f'{books1}')

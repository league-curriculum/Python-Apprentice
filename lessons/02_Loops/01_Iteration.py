# %% [markdown]
# # First Look at Lists
# 
# 
# Like we said before, a list is a lot like a list that you already know about, like a grocery list:
# 
# ```
# Things To Buy
#   - apples
#   - oranges
#   - bread 
#   - milk
# ```
# 
# But in Python we would write it like this: 
# 
# ```python 
# things_to_buy = [ 'apples','oranges','bread','milk']
# ```
# 
# The brackets, `[` and `]` are most often used to mean that something is a list. 
# 
# There are a lot of neat things we can do with a list.
# 
# First, you can get a specific item from a list, using the `[]` with a number inside. 
# 

# %% [markdown]
# 
# ```python
# things_to_buy[1]
# > oranges
# ```
# 
# Getting values out of a list like this is called "indexing".
# 
# 
# Like most programming languages, the first item in a list is 0, not 1, so if
# you wanted to get `apples` from the list, you would write `things_to_get[0]`
# 
# Another important thing about lists is you can _iterate_ them, which means 'do
# something repeatedly'. Here is how we would print out all of the items in the
# list: 
# 
# %% [python]

things_to_buy = [ 'apples','oranges','bread','milk']
 
for item in things_to_buy:
    print(item)


# %% [markdown]
# Loops and lists could be very useful for our turtle programs. For instance, we could make a square with 
# a different color on each side: 
# 
# ```python
# import turtle
# tina = turtle.Turtle()
# tina.shape("turtle")
# 
# forward = 50
# left = 90
# colors = [ 'red', 'blue', 'black', 'orange']
# 
# for color in colors:
#     tina.color(color)
#     tina.forward(forward)
#     tina.left(left)
# 
# ```
# 
# Or, we could change the angle that tina turns: 
# 
# ```python
# import turtle
# tina = turtle.Turtle()
# tina.shape("turtle")
# 
# forward = 50
# 
# for left in [ 45, 60, 90, 45, -90, 60, 22 , -45, 90]:
#     tina.forward(forward)
#     tina.left(left)
# 
# ```
# 
# 
# Here is a way that we could change two variables at once, using array indexes:
# 
# 
# ```python
# import turtle
# tina = turtle.Turtle()
# tina.shape("turtle")
# 
# forward = 50
# lefts = [ 45, -60, 90, 45, -90, 60, 22 , -45 ]
# colors = [ 'red', 'blue', 'black', 'orange', 'red', 'blue', 'black', 'orange']
# 
# for  i in range(8):
#     left = lefts[i]
#     color = colors[i]
# 
#     tina.color(color)
#     tina.forward(forward)
#     tina.left(left)
# 
# ```
# 


# %% [markdown]
# # Iterating over Iterables
# 
# Here is the first simple list that you learned about earlier. 
# 
# ```python 
# things_to_buy = [ 'apples','oranges','bread','milk']
# ```
# 
# This variable, `things_to_buy` is interesting, because it is a list of
# strings, but the strings are also a list, a list of letters. And in Python, 
# lists and strings are a lot a like. So, let's learn more about them both. 
# 
# Both lists and strings are "iterables". Iteration means taking things one at a
# time, and "iterating" a list means that we will get the first thing in the
# list, then the second, and on, until there is nothing left in the list. We have
# seen iteration before, with loops. Here are two loops, 
# one iterating over a list, and another iterating over a string. 
# 
# 
# %% [python]

things_to_buy = [ 'apples','oranges','bread','milk']
 
print("Things to buy:")

for things in things_to_buy:
    print(things)
 
print("\nLetters in a string")

for letter in "Hello!":
    print(letter)
 
# %% [markdown]

 # Now change the program so that, in the second loop, 
 # the program prints an 'x' instead of an 'l'
 
 

# %% [markdown]
# ## Iterables
# 
# The for loop, which looks like `for <variable> in <iterable>` works by taking each one of the 
# things in the iterable, assigning it to the variable, then running the code in the body
# of the loop. 
# 
# But, then you wonder, what does the code we first used for loops do? The one with `range()`
# in it?
# 
# Well, `range()` is an iterable!. But it isn't a string or a list. It doesn't have anything in it. 
# It just gives you the next number. But, we can turn it into a list that does have things in it. Here is
# how: 
# 
# ```python
# 
# # Turn a range() into a list:
# 
# l = list(range(5, 10))
# print(l)
# 
# ```
# 
# ::: tip 
# The reason that range() is not a list is that if you had a big range, like range(1_000_000_000), 
# Python would have to store a billion numbers, and would run out of memory. But range() doesn't actually store all of those numbers, it just counts up by 1, so it doesn't take a lot of memory )
# :::
# 
# 
# Then you put something inside `list()`, list will try to iterate the thing, and then take each 
# item and put it into a list. A string, like 'Hello World' is not a list, but we can turn it into 
# a list. 
# 
# 
# ```python
# 
# # Turn a stringinto a list:
# 
# l = list("Hello World!")
# print(l)
# 
# ```
# 
# You can turn a string into a list. The first way breaks the list into letters ( which programmers call "characters". The second way breaks the list at a specific character. 
# 
# ```python
# 
# # A list of letters
# l = list('adefibhgc')
# print(l)
# 
# # split a string at the comma character
# s = 'One,Two,Three,Four'
# l = s.split(',')
# 
# 
# ```
# 
# ## Sorting
# 
# Wait, those letters are out of order. Let's put them back in order. There are two ways: 
# 
# ```python
# 
# l = list('adefibhgc')
# l.sort()
# print(l)
# print()
# 
# l = list('adefibhgc')
# l = sorted(l)
# print(l)
# ```
# 
# ## Adding To Lists
# 
# You can add items to lists with `.append()`, and concatenate lists ( put them
# together) with `+`:
# 
# %% [python]
# 
# l = []
# 
# l.append('item 1')
# l.append('item 2')
# l.append('item 3')
# 
# l  = l + ['item 4', 'item 5']
# 
# print(l)

# %% [markdown]
# 
# Try adding more items to the list!
# 
# %% [python]



# %% [markdown]
# # Show Us Your Lists!
# 
# Now, you can write a program. Here is what your program should do. 
# 
# * Start with a string that has friend names, with spaces between the friend names, like
# this, but with real names: `'foo bar baz'`. Split the list into a string.
# * Ask the user for new friend names three times, and add those names to the list
# * Sort the list
# * Print out each name on a seperate line. 
# 

# %% [python]
# 

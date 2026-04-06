from guizero import App, Box, Text, TextBox, PushButton, ListBox, error

"""
Funny Words Dictionary

This program provides a graphical user interface (GUI) for managing a dictionary
of funny words and their definitions. Users can add new definitions, delete
existing definitions, and view the list of definitions in a listbox. 

The module uses the guizero library to create the GUI components and handle user
interactions.  It defines several functions for adding and deleting definitions,
as well as checking if a definition is funny. The definitions are stored in a
global dictionary called 'db'. To use the application, run the script and a
window will appear with input fields for entering a word and its definition.
Clicking the 'Add' button will add the definition to the dictionary and update
the listbox. Selecting a definition from the listbox and clicking the 'Delete
Selected' button will remove the definition from the dictionary. 

The module has a limit of storing up to 5 definitions. If the limit is reached,
an error message will be displayed and new definitions will not be added.
"""

# Implement the functions below

def add_definition(db, key, value):
    """
    Add a new definition to the database.

    Parameters:
    - db (dict): The database to add the definition to.
    - key (str): The key for the new definition.
    - value (str): The value for the new definition.

    Returns:
    - None

    If there are already 5 items in the database, an error message is displayed and the new item is not added.
    """

    # Check the limit

    # Set the item in the database

    pass


def delete_definition(db, key):
    """
    Deletes the definition associated with the given key from the database.

    Args:
        db (dict): The database containing the key-value pairs.
        key: The key to be deleted from the database.

    Returns:
        None
    """

    # Delete the item from db if it is present

    pass


def is_funny(definition):
    """
    Check if the definition is funny, which means it contains one of the words:

        'fun', 'funny', 'hilarious', 'amusing', 'pants', 'spleen'

    Args:
        definition (str): The definition to check.

    Returns:
        bool: True if the definition contains any of the funny words, False otherwise.
    """
    
    # Return True if the definition contains any of the funny words, False otherwise

    return False

def update_listbox(db):
    """
    Update the listbox with the current definitions in the database.

    Returns:
        list of str: A list of strings containing the definitions to be displayed in the listbox.
    """

    # This function will return a list of definitions to be displayed in the listbox, like
    # the one below. (For your function, you should set this list to the empty list)
    l = [
        "Item 1: Fake Definition 1",
        "Item 2: Fake Definition 2",
        "Item 3: fake Definition 3"
    ]

    # Add each definition to a string
    # iterate over the dict's key-value pairs and turn them into
    # strings, then add the strings to the list with .append()

    return l

# ================================================================

# Function to add a definition

def _add_definition():
    word = word_entry.value.strip()
    definition = definition_entry.value.strip()
    

    if word and definition:
        if is_funny(definition):
            definition = "😂 " + definition + " 🤡"
        add_definition(db, word, definition)
        _update_listbox(db)
        word_entry.clear()
        definition_entry.clear()
    else:
        error("Input Error", "Both fields must be filled out.")

# Global dictionary to store definitions
db = {}

# Function to update the listbox with current definitions
def _update_listbox(db):
    listbox.clear()
    for i in update_listbox(db):
        listbox.append(i)

# Function to delete a definition
def _delete_definition():
    selected_item = listbox.value
    if selected_item:
        word = selected_item.split(":", 1)[0].strip()
        if word in db:
            del db[word]
            _update_listbox(db)

# Main app
app = App(title="Funny Definitions", width=600, height=300)

# Top pane for input
top_pane = Box(app, align="top", width="fill", border=True)

Text(top_pane, text="Word:", align="left")
word_entry = TextBox(top_pane, width="10", align="left")
Text(top_pane, text="Definition:", width="10" , align="left")
definition_entry = TextBox(top_pane, width="25", align="left")
PushButton(top_pane, text="Add", width="5", align="bottom", command=_add_definition)

# Bottom pane for displaying definitions
bottom_pane = Box(app, align="bottom", width="fill", height="fill", border=True)
listbox = ListBox(bottom_pane, items=[], width="fill", height="fill")
PushButton(bottom_pane, text="Delete Selected", command=_delete_definition)

# Function to handle enter key press
def handle_enter(event):
    if event.tk_event.keysym == "Return":
        _add_definition()

# Bind enter key press event to handle_enter function
app.when_key_pressed = handle_enter

_update_listbox(db) # Initial update of listbox

app.display()
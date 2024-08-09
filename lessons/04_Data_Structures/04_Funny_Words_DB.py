from guizero import App, Box, Text, TextBox, PushButton, ListBox, error

"""Funny Words Dictionary

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


# Implement the three functions below


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


################################################################

# Function to add a definition

def _add_definition():
    word = word_entry.value.strip()
    definition = definition_entry.value.strip()
    

    if word and definition:
        if is_funny(definition):
            definition = "😂 " + definition + " 🤡"
        add_definition(db, word, definition)
        update_listbox()
        word_entry.clear()
        definition_entry.clear()
    else:
        error("Input Error", "Both fields must be filled out.")

# Global dictionary to store definitions
db = {}

# Function to update the listbox with current definitions
def update_listbox():
    listbox.clear()
    for word, definition in db.items():
        listbox.append(f"{word}: {definition}")

# Function to delete a definition
def _delete_definition():
    selected_item = listbox.value
    if selected_item:
        word = selected_item.split(":", 1)[0].strip()
        if word in db:
            del db[word]
            update_listbox()

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
    if event.key == "Enter":
        _add_definition()

# Bind enter key press event to handle_enter function
app.when_key_pressed = handle_enter

app.display()


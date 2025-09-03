import os #gives program access to Python’s OS (Operating System) module. which provides functions to interact with the file system and environment in a platform-independent way.
import tkinter as tk #Import everything from Tkinter (GUI toolkit)
import random # Import Python's random module for random choices.

# Get absolute path of the icon in the same folder as the script
base_dir = os.path.dirname(os.path.abspath(__file__)) 
icon_path = os.path.join(base_dir, "icon.ico")

#make window
window = tk.Tk() # Create the main application window (the root Tk object).
window.title("Activity Picker")  #Set the window title text.
window.iconbitmap(icon_path) # Set the window icon.
window.geometry("300x300") # Set the initial window size: width=300 px, height=300 px.

#list options
hobbies = []
break_Activities = []

#populate list with text files
with open('hobbies.txt', 'r') as hobby_file, open('breaks.txt', 'r') as break_file:
    #hobbies
    for line in hobby_file:
        hobbies.append(line.strip())

    #breaks
    for line in break_file:
        break_Activities.append(line.strip())

#functions
def hobby_picker():
    if len(hobbies) == 0:
        return "There's nothing here mate."
    else:
        x = random.choice(hobbies) # Randomly pick one item from your hobby list.
        return x                   # Return the chosen hobby.

def break_picker():
    if len(break_Activities) == 0:
        return "There's nothing here mate."
    else:
        x = random.choice(break_Activities) # Randomly pick one break activity.
        return x                            # Return the chosen break activity.

def home():
    # This function returns the UI to the "main menu" by hiding result widgets and showing the two main buttons again.
    result_Label.pack_forget() # Hide the result label if it’s visible.
    retryHob_But.pack_forget() # Hide the hobby retry button.
    retryBreak_But.pack_forget() # Hide retry break button
    return_But.pack_forget() # Hide the "Main Menu" button.

    # clean activity buttons
    add_Hobby_But.pack_forget()
    add_Break_But.pack_forget()
    add_Both_But.pack_forget()
    add_label.pack_forget()

    # clean entry and save
    entry.pack_forget()
    save_button.pack_forget()
    
    hobby_But.pack() # Show the "Hobby" button.
    break_But.pack() # Show the "Break" button.
    add_Activity_But.pack()

#hobby window
#answer, retry button, go back to main
def hobby_page():
    # clean main screen
    break_But.pack_forget() # Hide the "Break" button.
    hobby_But.pack_forget() # Hide the "Hobby" button.
    retryBreak_But.pack_forget() # Hide the retry button for breaks.

    # clean activity buttons
    add_Activity_But.pack_forget()
    add_Hobby_But.pack_forget()
    add_Break_But.pack_forget()
    add_Both_But.pack_forget()
    add_label.pack_forget()

    # clean entry and save
    entry.pack_forget()
    save_button.pack_forget()
   
    result = hobby_picker() # Pick a random hobby.
    result_Label.config(text = result) #display the hobby text in the label
    result_Label.pack() #show the label

    retryHob_But.pack() #show the retry button for hobbies.
    return_But.pack() #show the main menu button to go back

def hobby_retry():
    result = hobby_picker() # pick a random hobby
    result_Label.config(text = result) # set the label to the random hobby
    result_Label.pack() # display the result

#break window
#answer, retry, go back to main
def break_page():
    # Hide main menu buttons.
    break_But.pack_forget() 
    hobby_But.pack_forget()

    # clean activity buttons
    add_Activity_But.pack_forget()
    add_Hobby_But.pack_forget()
    add_Break_But.pack_forget()
    add_Both_But.pack_forget()
    add_label.pack_forget()

    # clean entry and save
    entry.pack_forget()
    save_button.pack_forget()

    # Hide hobby retry button
    retryHob_But.pack_forget()

    result = break_picker() # Pick a random break activity.
    result_Label.config(text = result) # Display the result
    result_Label.pack() # show the label

    retryBreak_But.pack() # show the retry button for breaks
    return_But.pack() # Show the "Main Menu" button.


def break_retry():
    result = break_picker() # pick a random break activity
    result_Label.config(text = result) # set the label to the random activity
    result_Label.pack() # display the result

# add activity window
# select add break, hobby or both
def add_activity():
    # Hide main menu buttons
    hobby_But.pack_forget()
    break_But.pack_forget()
    add_Activity_But.pack_forget()

    # Show label and buttons
    add_label.pack()
    add_Hobby_But.pack()
    add_Break_But.pack()
    add_Both_But.pack()
    return_But.pack()  # allow going back

def show_input(activity_type):
    # Hide the three buttons
    add_Hobby_But.pack_forget()
    add_Break_But.pack_forget()
    add_Both_But.pack_forget()
    add_label.pack_forget()

    # Entry for user input
    entry.pack()
    save_button.config(command=lambda: save_activity(activity_type))
    save_button.pack()


def save_activity(activity_type):
    new_item = entry.get().strip()
    if new_item:
        if activity_type == "hobby":
            hobbies.append(new_item)
            with open('hobbies.txt', 'a') as f:
                f.write(new_item + '\n')
        elif activity_type == "break":
            break_Activities.append(new_item)
            with open('breaks.txt', 'a') as f:
                f.write(new_item + '\n')
        else:  # both
            hobbies.append(new_item)
            break_Activities.append(new_item)
            with open('hobbies.txt', 'a') as f:
                f.write(new_item + '\n')
            with open('breaks.txt', 'a') as f:
                f.write(new_item + '\n')

    # Hide entry and save button
    entry.delete(0, tk.END)
    entry.pack_forget()
    save_button.pack_forget()

    # Back to main menu
    home()




#main window
#3 buttons hobby or break or add activity
hobby_But = tk.Button(window, text = "Hobby", command= hobby_page) # Create the "Hobby" button: clicking runs hobby_page().
hobby_But.pack() # Place it on the window using pack() layout manager.

break_But = tk.Button(window, text = "Break", command = break_page) # Create the "Break" button.
break_But.pack() # Place it.

add_Activity_But = tk.Button(window, text = "Add Activity", command=add_activity) # Create the Add Activity Button.
add_Activity_But.pack() # Place it

# Create buttons to add different types of activities (initially not packed)
add_Hobby_But = tk.Button(window, text="Hobby", command=lambda: show_input("hobby"))
add_Break_But = tk.Button(window, text="Break", command=lambda: show_input("break"))
add_Both_But = tk.Button(window, text="Both", command=lambda: show_input("both"))
add_label = tk.Label(window, text="What kind of activity would you like to add?")

return_But = tk.Button(window, text = "Main \n Menu", command = home)  # Create the "Main Menu" button (initially not packed).

result_Label = tk.Label(window, text = "Default") # Create a label to show results (initially not packed).

# create the hobby and break retry buttons (initially not packed)
retryHob_But = tk.Button(window, text = "Retry", command = hobby_retry)
retryBreak_But = tk.Button(window, text = "Retry", command = break_retry)

entry = tk.Entry(window)
save_button = tk.Button(window, text="Save")

#display window
window.mainloop()
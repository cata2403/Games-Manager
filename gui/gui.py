import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

from service.serv import GameService


def save_game(popup, treeview, name_entry, genres_entry, status_combobox, score_spin, service:GameService):

    name = name_entry.get().strip()
    genres = genres_entry.get().strip()
    status = status_combobox.get().strip()

    try:
        score = int(score_spin.get())
        print(type(score))
        service.addGame(name, genres, score, status)
    except ValueError:
        return "Eroare"

    if not (name and genres and status):
        msgbox.showerror("Incomplete", "All fields must be completed!", parent = popup)
        return
    if not (0 <= score <= 100):
        msgbox.showerror("Invalid score", "The score must be between 0 and 100!", parent = popup)
        return

    row_tag = status.lower()
    treeview.insert("", tk.END, values=(name, genres, status, score), tags=(row_tag,))

    popup.destroy()

def update_game(popup, treeview, item_id, name_entry, genres_entry, status_combobox, score_spin, service:GameService):

    name= name_entry.get().strip()
    genres = genres_entry.get().strip()
    status = status_combobox.get().strip()

    try:
        score = int(score_spin.get())
        service.modifyGame(name,genres,score,status)
    except ValueError:
        score = -1

    if not (name and genres and status):
        msgbox.showerror("Incomplete", "All fields must be completed!", parent = popup)
        return
    if not (0 <= score <= 100):
        msgbox.showerror("Invalid score", "The score must be between 0 and 100!", parent = popup)
        return

    row_tag = status.lower()
    treeview.item(item_id, values=(name, genres, status, score), tags=(row_tag,))
    popup.destroy()

def open_add_popup(root, treeview, service):

    popup = tk.Toplevel(root)
    popup.title("Add Game")
    popup.resizable(False, False)
    popup.grab_set()

    name_label = ttk.Label(popup, text = "Name:")
    genres_label = ttk.Label(popup, text = "Genres:")
    status_label = ttk.Label(popup, text = "Status:")
    score_label = ttk.Label(popup, text = "Score (0‑100):")

    name_label.grid(row = 0, column=0, padx = (10,0), pady = 5, sticky = "e")
    genres_label.grid(row = 1, column = 0, padx = (10,0), pady = 5, sticky = "e")
    status_label.grid(row = 2, column = 0, padx = (10,0), pady = 5, sticky = "e")
    score_label.grid(row = 3, column = 0, padx = (20,0), pady = 5, sticky = "e")

    name_entry = ttk.Entry(popup, width = 30)
    genres_entry = ttk.Entry(popup, width = 30)
    status_combobox = ttk.Combobox(popup, values = ["Finished", "Ongoing", "Upcoming"], state = "readonly", width = 15)
    status_combobox.set("Finished")
    score_spin = ttk.Spinbox(popup, from_ = 0, to = 100, width = 5)

    name_entry.grid(row = 0, column = 1, padx = (0,10), pady = 5, sticky = "w")
    genres_entry.grid(row = 1, column = 1, padx = (0,10), pady = 5, sticky = "w")
    status_combobox.grid(row = 2, column = 1, padx = (0,10), pady = 5, sticky = "w")
    score_spin.grid(row = 3, column = 1, padx = (0,10), pady = 5, sticky = "w")

    score_spin.delete(0, tk.END)
    score_spin.insert(0, "0")

    add_button = ttk.Button(popup, text = "Add",command = lambda: save_game(popup, treeview, name_entry, genres_entry, status_combobox, score_spin, service))
    add_button.grid(row = 4, column = 0, columnspan = 2, pady = 10)

    name_entry.focus()

def open_edit_popup(root, treeview, service):

    selected = treeview.selection()
    if not selected:
        msgbox.showinfo("No selection", "Please select a game to edit!")
        return
    if len(selected) > 1:
        msgbox.showinfo("Multiple selection", "Please select just one game to edit!")
        return
    item_id = selected[0]
    current_name, current_genres, current_status, current_score = treeview.item(item_id, "values")

    popup = tk.Toplevel(root)
    popup.title("Edit Game")
    popup.resizable(False, False)
    popup.grab_set()

    name_label = ttk.Label(popup, text = "Name:")
    genres_label = ttk.Label(popup, text = "Genres:")
    status_label = ttk.Label(popup, text = "Status:")
    score_label = ttk.Label(popup, text = "Score (0‑100):")

    name_label.grid(row = 0, column = 0, padx = (10, 0), pady = 5, sticky = "e")
    genres_label.grid(row = 1, column = 0, padx = (10, 0), pady = 5, sticky = "e")
    status_label.grid(row = 2, column = 0, padx = (10, 0), pady = 5, sticky = "e")
    score_label.grid(row = 3, column = 0, padx = (20, 0), pady = 5, sticky = "e")

    name_entry = ttk.Entry(popup, width = 30)
    genres_entry = ttk.Entry(popup, width = 30)
    status_combobox = ttk.Combobox(popup, values = ["Finished", "Ongoing", "Upcoming"], state = "readonly", width = 15)
    score_spin = ttk.Spinbox(popup, from_ = 0, to = 100, width = 5)

    name_entry.grid   (row = 0, column = 1, padx = (0,10), pady = 5, sticky = "w")
    genres_entry.grid (row = 1, column = 1, padx = (0,10), pady = 5, sticky = "w")
    status_combobox.grid(row = 2, column = 1, padx = (0,10), pady = 5, sticky = "w")
    score_spin.grid   (row = 3, column = 1, padx = (0,10), pady = 5, sticky = "w")

    name_entry.insert(0, current_name)
    genres_entry.insert(0, current_genres)
    status_combobox.set(current_status)
    score_spin.delete(0, tk.END)
    score_spin.insert(0, current_score)

    edit_button = ttk.Button(popup, text = "Save changes",command = lambda: update_game(popup, treeview, item_id, name_entry, genres_entry, status_combobox, score_spin, service))
    edit_button.grid(row = 4, column = 0, columnspan = 2, pady = 10)

    name_entry.focus()

def delete_selected(treeview, service:GameService):

    selected_games = treeview.selection()
    if not selected_games:
        msgbox.showinfo("Nothing selected", "Please select a game to delete!")
        return
    confirm = msgbox.askyesno(title = "Confirmation", message = f"Are you sure you want to delete {len(selected_games)} games?"
    )
    if not confirm:
        return
    for item_id in selected_games:
        item_details = treeview.item(item_id)
        values = item_details.get("values")
        service.deleteGame(values[0])
        treeview.delete(item_id)

def clear_selected(event, service):

    tree = event.widget
    if not tree.identify_row(event.y):
        tree.selection_remove(tree.selection())

def load_data(treeview, games_list):

    clear_all(treeview)
    for game in games_list:
        name, genres, status, score = game.get_name(), game.get_type(), game.get_status(), game.get_rating()
        treeview.insert("", tk.END, values=(name, genres, status, score))


def clear_all(tree):

   for item in tree.get_children():
      tree.delete(item)

def mainwindow(service:GameService):

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Game Manager")

    searchbar_frame = ttk.Frame(root)
    searchbar_frame.grid(row = 0, column = 0, columnspan = 3)

    searchbar_entry = ttk.Entry(searchbar_frame, width = 25)
    searchbar_entry.grid(row = 0, column = 1, pady = (5,0))
    search_button = ttk.Button(searchbar_frame, text = "Search", command = lambda: load_data(games_tree, service.filterByName(searchbar_entry.get().strip())))
    search_button.grid(row = 0, column = 2, pady = (5,0), sticky = "W")

    add_button = ttk.Button(root, text = "Add", command = lambda: open_add_popup(root, games_tree, service))
    add_button.grid(row = 1, column = 0, padx = 30, pady = 15)
    edit_button = ttk.Button(root, text = "Edit", command = lambda: open_edit_popup(root, games_tree, service))
    edit_button.grid(row = 1, column = 1, padx = 30, pady = 15)
    delete_button = ttk.Button(root, text = "Delete", command = lambda: delete_selected(games_tree, service))
    delete_button.grid(row = 1, column = 2,  padx = 30, pady = 15)

    combobox = ttk.Combobox(root ,values = ["All", "Finished", "Ongoing", "Upcoming"], state = "readonly")
    combobox.set("Status")
    combobox.grid(row = 2, column = 0, padx = (15,0), sticky = "W")

    columns = ("Name", "Genres", "Status", "Score")
    games_tree = ttk.Treeview(root, columns = columns, show = "headings", height=8)
    games_tree.grid(row = 3, column = 0, padx=(15,15), pady = (10, 10), columnspan=3)
    for col in columns:
        games_tree.column(col, anchor = "center")
        games_tree.heading(col, text = col, anchor = "center")
    games_tree.tag_configure("finished", background="#c9f7c2")
    games_tree.tag_configure("ongoing", background="#fff6b3")
    games_tree.tag_configure("upcoming", background="#c7e9ff")

    load_data(games_tree, service.getAllGames())

    root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random


class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Adventure Game")

        self.name = ""
        self.character = ""
        self.floor_rooms = {
            "Floor 1: The Arcane Sanctuary": [
                "Room of Whispers",
                "The Alchemist's Lab",
                "Chamber of Shadows",
            ],
            "Floor 2: The Cursed Catacombs": [
                "Pit of Forgotten Souls",
                "Hall of Broken Dreams",
                "Crypt of the Damned",
            ],
            "Floor 3: The Abyssal Throne": [
                "Void's Edge",
                "Hall of the Lich King",
                "The Eternal Forge",
            ],
        }
        self.enemies = ["Goblin", "Orc", "Dragon", "Troll"]
        self.items = ["Healing Potion", "Magic Sword", "Shield"]
        self.explored_rooms = []

        self.main_menu()

    def main_menu(self):
        self.clear_frame()

        greeting_label = tk.Label(
            self.root, text="Welcome to the Adventure Game!", font=("Arial", 16)
        )
        greeting_label.pack(pady=10)

        name_label = tk.Label(self.root, text="Enter your name:")
        name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        start_button = tk.Button(self.root, text="Start", command=self.get_name)
        start_button.pack(pady=10)

    def get_name(self):
        self.name = self.name_entry.get()
        if self.name:
            self.character_selection()
        else:
            messagebox.showerror("Error", "Please enter your name!")

    def character_selection(self):
        self.clear_frame()

        label = tk.Label(
            self.root,
            text=f"Hello, {self.name}! Choose your character:",
            font=("Arial", 14),
        )
        label.pack(pady=10)

        dwarf_button = tk.Button(
            self.root, text="Dwarf", command=lambda: self.set_character("Dwarf")
        )
        dwarf_button.pack(pady=5)

        elf_button = tk.Button(
            self.root, text="Elf", command=lambda: self.set_character("Elf")
        )
        elf_button.pack(pady=5)

    def set_character(self, character):
        self.character = character
        self.lobby()

    def lobby(self):
        self.clear_frame()

        label = tk.Label(
            self.root,
            text=f"Welcome to the Lobby, {self.name} the {self.character}!",
            font=("Arial", 14),
        )
        label.pack(pady=10)

        floor_label = tk.Label(self.root, text="Choose a floor to explore:")
        floor_label.pack(pady=10)

        floor_1_button = tk.Button(
            self.root,
            text="Floor 1: The Arcane Sanctuary",
            command=lambda: self.show_rooms("Floor 1: The Arcane Sanctuary"),
        )
        floor_1_button.pack(pady=5)

        floor_2_button = tk.Button(
            self.root,
            text="Floor 2: The Cursed Catacombs",
            command=lambda: self.show_rooms("Floor 2: The Cursed Catacombs"),
        )
        floor_2_button.pack(pady=5)

        floor_3_button = tk.Button(
            self.root,
            text="Floor 3: The Abyssal Throne",
            command=lambda: self.show_rooms("Floor 3: The Abyssal Throne"),
        )
        floor_3_button.pack(pady=5)

    def show_rooms(self, floor):
        self.clear_frame()

        label = tk.Label(self.root, text=f"{floor}: Choose a room", font=("Arial", 14))
        label.pack(pady=10)

        for room in self.floor_rooms[floor]:
            if room not in self.explored_rooms:
                room_button = tk.Button(
                    self.root, text=room, command=lambda r=room: self.enter_room(r)
                )
                room_button.pack(pady=5)

    def enter_room(self, room):
        self.clear_frame()

        self.explored_rooms.append(room)
        encounter_label = tk.Label(
            self.root, text=f"You have entered {room}.", font=("Arial", 14)
        )
        encounter_label.pack(pady=10)

        enemy = random.choice(self.enemies)
        enemy_label = tk.Label(
            self.root, text=f"A wild {enemy} appears!", font=("Arial", 12)
        )
        enemy_label.pack(pady=5)

        item = random.choice(self.items)
        item_label = tk.Label(
            self.root, text=f"You found a {item}!", font=("Arial", 12)
        )
        item_label.pack(pady=5)

        fight_button = tk.Button(
            self.root, text="Fight", command=lambda: self.fight(enemy, item)
        )
        fight_button.pack(pady=10)

    def fight(self, enemy, item):
        result = random.choice(["win", "lose"])
        if result == "win":
            messagebox.showinfo(
                "Victory!", f"You defeated the {enemy} using the {item}!"
            )
        else:
            messagebox.showinfo("Defeated!", f"The {enemy} was too strong!")

        if len(self.explored_rooms) == sum(
            len(rooms) for rooms in self.floor_rooms.values()
        ):
            self.win_game()
        else:
            self.lobby()

    def win_game(self):
        self.clear_frame()

        label = tk.Label(
            self.root,
            text=f"Congratulations, {self.name}! You have explored all the rooms and won the game!",
            font=("Arial", 14),
        )
        label.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Main game execution
root = tk.Tk()
game = AdventureGame(root)
root.mainloop()

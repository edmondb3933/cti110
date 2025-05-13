# Brandon Edmond
# 5/5/25
# P5HW
# A program that simulates a simple character creation game using loops, functions, and module import.

import random

# 🎮 Value-returning function to create a character
def create_character():
    print("👾 Let's create your character!")
    name = input("Enter your character's name: ")
    health = 100
    attack_points = random.randint(10, 20)
    inventory = []

    character = {
        "name": name,
        "health": health,
        "attack_points": attack_points,
        "inventory": inventory
    }
    return character

# 📋 Non-value-returning function to display character info
def display_character(character):
    print("\n📜 Character Summary:")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")
    print()

# 🗡️ Game logic: simple battle with a random enemy
def battle(character):
    enemy_health = random.randint(50, 120)
    enemy_attack = random.randint(5, 15)
    print(f"\n💀 An enemy appears with {enemy_health} health and {enemy_attack} attack power!")

    while enemy_health > 0 and character["health"] > 0:
        action = input("Do you want to (a)ttack or (r)un? ").lower()
        if action == 'a':
            damage = random.randint(5, character["attack_points"])
            enemy_health -= damage
            print(f"🗡️ You hit the enemy for {damage} damage. Enemy health: {enemy_health}")
            if enemy_health <= 0:
                print("🎉 You defeated the enemy!")
                item = random.choice(["💎 gem", "🧪 potion", "🗝️ key"])
                character["inventory"].append(item)
                print(f"You found a {item}!")
                break
            # Enemy attacks back
            hit = random.randint(0, enemy_attack)
            character["health"] -= hit
            print(f"⚔️ The enemy hits you for {hit} damage. Your health: {character['health']}")
        elif action == 'r':
            print("🏃 You ran away!")
            break
        else:
            print("Invalid choice. Try again.")

# 🧪 Game logic: random event adventure
def random_event(character):
    print("\n🌲 You venture into the forest...")
    event = random.choice(["treasure", "trap", "nothing"])
    
    if event == "treasure":
        reward = random.choice(["📜 ancient scroll", "🧥 magic cloak", "💰 gold coins"])
        character["inventory"].append(reward)
        print(f"You found a {reward}!")
    elif event == "trap":
        damage = random.randint(5, 30)
        character["health"] -= damage
        print(f"💥 You triggered a trap and lost {damage} health!")
    else:
        print("🌿 Nothing happens... peaceful but uneventful.")

# 🎯 Main function
def main():
    print("🧙 Welcome to the Character Creation Game!")
    character = create_character()

    while True:
        print("\nWhat would you like to do?")
        print("1. Display character")
        print("2. Go into battle")
        print("3. Explore the world")
        print("4. Exit game")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_character(character)
        elif choice == "2":
            battle(character)
        elif choice == "3":
            random_event(character)
        elif choice == "4":
            print("👋 Thanks for playing! Goodbye.")
            break
        else:
            print("❌ Invalid choice, please try again.")

        if character["health"] <= 0:
            print("💀 Your character has died. Game over.")
            break

# Run the main function
if __name__ == "__main__":
    main()

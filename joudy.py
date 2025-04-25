import time
import sys
import random

points = 0
win_score = 0
lose_score = 0

def display_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_valid_input():
    while True:
        choice = input("Choose 1 or 2: ")
        if choice in ["1", "2"]:
            return choice
        else:
            display_text("⚠️ Please enter 1 or 2.")

def show_scores():
    global points, win_score, lose_score
    print(f"\n🏆 Win Score: {win_score}")
    print(f"💀 Lose Score: {lose_score}")
    print(f"⭐ Total Points: {points}\n")

def scene_one(player_name):
    global points, win_score, lose_score
    points = 0
    win_score = 0
    lose_score = 0
    display_text(f"\nWelcome {player_name}, your mission begins now!", 0.04)
    time.sleep(1)
    display_text("🚀 Mission: Explore a mysterious planet known as 'The Cursed Planet'.", 0.04)
    display_text("A strange signal has been received from this planet. You and your 3 team members are on a mission to discover its origin.", 0.04)
    display_text("Team Members:\n1. Dr. Sara - Alien language expert\n2. Captain Marwa - Ship engineer\n3. Khadiga - Smart AI assistant\n")
    display_text("Scene 1: Approaching the planet", 0.05)
    display_text("🚀 You are now in the planet's orbit, and the visibility is extremely low. What do you do?")
    display_text("1. Land immediately on the surface")
    display_text("2. Circle the planet and gather information first")

    choice1 = get_valid_input()
    if choice1 == "1":
        display_text("❌ You land immediately... but a storm hits and damages the ship!")
        points -= 1
        lose_score += 1
    else:
        display_text("✅ You circle the planet and gather useful data. Smart choice!")
        points += 2
        win_score += 1

    show_scores()

    display_text("🚪 You find a large building. It's dark inside. What do you do?")
    display_text("1. Enter with Captain Marwa.")
    display_text("2. Send Khadiga in alone.")
    choice2 = get_valid_input()
    if choice2 == "1":
        display_text("✅ Teamwork! You enter safely and discover a hidden hall.")
        points += 2
        win_score += 1
    else:
        display_text("❌ Khadiga disappears inside... not good.")
        points -= 1
        lose_score += 1

    show_scores()

    display_text("👾 Before leaving the spaceship, what should the team do?")
    display_text("1. Wear protective suits and check oxygen levels.")
    display_text("2. Go out quickly to save time.")
    choice3 = get_valid_input()
    if choice3 == "1":
        display_text("✅ Excellent! Safety first is always the best choice.")
        points += 2
        win_score += 1
    else:
        display_text("❌ Dangerous move! The planet's atmosphere might be toxic.")
        points -= 1
        lose_score += 1

    show_scores()

    if points < 3:
        display_text("😞 You didn’t collect enough points to continue. Restarting the game...\n")
        return False
    else:
        display_text("✅ You've passed Scene 1 successfully!\n")
        return True

def scene_two():
    global points, win_score, lose_score

    display_text("🌌 Scene 2: Inside the Mysterious Building")
    display_text("Strange writings glow on the wall.")
    display_text("🌒 You find two doors. One has light coming from it. The other is silent and dark.")
    display_text("1. Enter the door with light.")
    display_text("2. Enter the dark silent door.")
    choice1 = get_valid_input()
    if choice1 == "2":
        display_text("✅ The dark door leads to a secret lab with alien tech!")
        points += 2
        win_score += 1
    else:
        display_text("❌ The light room is a trap! A gas fills the room.")
        points -= 1
        lose_score += 1

    show_scores()

    display_text("📜 You discover an alien terminal asking for a code. What do you do?")
    display_text("1. Let Khadiga try guessing the code.")
    display_text("2. Use symbols decoded earlier with Dr. Sara.")
    choice2 = get_valid_input()
    if choice2 == "2":
        display_text("✅ The code works! A hidden path opens.")
        points += 2
        win_score += 1
    else:
        display_text("❌ Wrong code. The system shuts down temporarily.")
        points -= 1
        lose_score += 1

    show_scores()

    display_text("⚠️ An alarm starts. You must choose a way out quickly.")
    display_text("1. Use emergency escape pod.")
    display_text("2. Follow the tunnel beneath the lab.")
    choice3 = get_valid_input()
    if choice3 == "2":
        display_text("✅ Tunnel leads to an ancient underground city!")
        points += 2
        win_score += 1
    else:
        display_text("❌ Escape pod is damaged. You barely survive.")
        points -= 1
        lose_score += 1

    show_scores()

    if points < 6:
        display_text("😞 You didn’t gather enough knowledge. The mission ends here.\n")
        return False
    else:
        display_text("🎉 Congratulations! You passed Two Scene  successfully!\n")
        return True
time.sleep(2)
def scene_three():
    global points, win_score, lose_score

    display_text("🏛️ Scene 3: The Ancient City Awakens...", 0.05)
    time.sleep(1)
    display_text("Strange machines begin activating... It feels like you're being watched. 👁️", 0.04)
    display_text("🚀 You reach a large circular chamber with a glowing crystal in the center.")
    display_text("1. Touch the crystal to see what happens.")
    display_text("2. Scan it using your AI assistant Khadiga.")
    choice1 = get_valid_input()
    if choice1 == "2":
        display_text("✅ Smart move! Khadiga scans it and reveals it's a power source.")
        points += 2
        win_score += 1
    else:
        display_text("❌ The crystal emits a shockwave. You lose time recovering.")
        points -= 1
        lose_score += 1

    show_scores()

    display_text("🚨 Suddenly, robotic guardians activate around you!")
    display_text("1. Try to communicate using alien symbols.")
    display_text("2. Run and hide behind ancient pillars.")
    choice2 = get_valid_input()
    if choice2 == "1":
        display_text("✅ You calm them down using alien language.")
        points += 2
        win_score += 1
    else:
        display_text("❌ You hide but get spotted. They chase you.")
        points -= 1
        lose_score += 1

    show_scores()

    display_text("📡 You find a control panel that can send a message to Earth.")
    display_text("1. Send a message revealing the city’s secrets.")
    display_text("2. Stay silent to protect the planet’s mysteries.")
    choice3 = get_valid_input()
    if choice3 == "2":
        display_text("✅ You earn the trust of the planet’s AI guardian. 🤖")
        points += 2
        win_score += 1
    else:
        display_text("❌ The message is blocked, and the system locks you out.")
        points -= 1
        lose_score += 1

    show_scores()

    if points < 10:
        display_text("😥 You needed more points to unlock the final secrets.")
        return False
    else:
        display_text("🎉 Congratulations! You’ve earned the title: 🌟 Planet Explorer Elite 🌟")
        display_text("You uncovered the truth behind The Cursed Planet and gained its ancient wisdom.")
        display_text("🌌 THE END - For now...")
        return True
time.sleep(4)
def scene_four():
    global points, win_score, lose_score

    display_text("✨ Scene 4: The Random Magic Wand!", 0.05)
    time.sleep(1)
    display_text("You found a mysterious wand... its color changes every time you hold it!", 0.04)
    time.sleep(1)

    wand_effects = {
        "Red": "You turned into a monkey! Funny... but not helpful.",
        "Blue": "A magical shield protected you from danger!",
        "Green": "You teleported to a safe location.",
        "Yellow": "The wand blasted a strong light at your enemies!",
        "Purple": "You got dizzy and lost some time.",
        "Black": "The wand disappeared... nothing happened."
    }

    chosen_color = random.choice(list(wand_effects.keys()))
    display_text(f"\nThe wand turned {chosen_color}!")
    display_text(wand_effects[chosen_color])

    if chosen_color in ["Blue", "Green", "Yellow"]:
        points += 2
        win_score += 1
    elif chosen_color in ["Purple", "Red" , "Black"]:
        points -= 1
        lose_score += 1

    show_scores()
    time.sleep(1)

    again = input("Do you want to try using the wand again? (yes/no): ").lower()
    if again == "yes":
        return scene_four()
    else:
        if points >= 12:
            display_text("🎉 You mastered the magic wand!")
            display_text("✨ You're now ready for the final adventure...")
        else:
            display_text("😕 You need more training with the wand. Try again later!")

    display_text("🚀 This is the end what do you want to do?")
    display_text("1. Make a book write in it all the secrets of this cursed planet")
    display_text("2. No ")
    choice1 = get_valid_input()
    if choice1 == "1":
        display_text("✅ it's a perfect choice.")
        points += 2
        win_score += 1
        show_scores()
        display_text("Over the time..............")
        display_text("After your death......")
        display_text("Your daughter (JOUDY) and your son (ASAAD)🧑👧 found your book 😲 ")
        time.sleep(3)
        display_text("Joudy and Asaad read your book and knew all the secretrs ")
        display_text("What Do you think Joudy and Asaad do ?")
        display_text("They went to this planet or no !!!")
        display_text("BY:JOUDY ELTOP")

    else:
        display_text("❌ With time you will forget what happened on this planet")
        points -= 1
        lose_score += 1
        show_scores()
        display_text("The game is end")

    
    return True


def start_game():
    display_text("🌌 Welcome to... THE CURSED PLANET 🌌", 0.05)
    time.sleep(1)
    display_text("👤 What's your name, brave explorer?")
    player_name = input("Name: ")
    display_text(f"🧑‍🚀 Nice to meet you, {player_name}! Let's begin...\n", 0.04)

    if scene_one(player_name):
        if scene_two():
            if scene_three():
                scene_four()
            else:
                start_game()
        else:
            start_game()
    else:
        start_game()

if __name__ == "__main__":
    start_game()

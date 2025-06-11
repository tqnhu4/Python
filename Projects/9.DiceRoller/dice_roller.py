import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def main():
    print("🎲 Welcome to the Dice Roller!")

    while True:
        try:
            num_dice = int(input("🔢 Enter the number of dice to roll (1–10): "))
            if not 1 <= num_dice <= 10:
                print("⚠️ Please enter a number between 1 and 10.")
                continue
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        results = roll_dice(num_dice)
        print(f"🎲 Results: {', '.join(str(r) for r in results)}")

        again = input("👉 Roll again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()

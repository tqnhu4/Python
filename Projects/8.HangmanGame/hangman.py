import random

# Danh sách từ mẫu (hoặc có thể load từ file)
WORD_LIST = ['python', 'flask', 'hangman', 'developer', 'keyboard', 'monitor']

def load_words_from_file(filename="words.txt"):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def get_random_word():
    return random.choice(WORD_LIST).lower()

#def get_random_word():
#    with open("words.txt") as f:
#        return random.choice(f.read().splitlines())    

def display_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("🎮 Chào mừng đến với trò chơi Hangman!")
    print(f"Từ cần đoán có {len(word)} chữ cái.")

    while wrong_guesses < max_wrong:
        print("\nTừ hiện tại:", display_progress(word, guessed_letters))
        print(f"Sai {wrong_guesses}/{max_wrong} lần")

        guess = input("Đoán 1 chữ cái: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Vui lòng chỉ nhập 1 chữ cái.")
            continue

        if guess in guessed_letters:
            print("⚠️ Bạn đã đoán chữ này rồi.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Đúng!")
        else:
            print("❌ Sai!")
            wrong_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Bạn đã thắng! Từ đúng là:", word)
            break
    else:
        print("\n💀 Bạn đã thua! Từ đúng là:", word)

if __name__ == "__main__":
    hangman()

import random
import string


class WordGuessingGame:
    """Manage the word-guessing game using object-oriented principles."""

    def __init__(self, max_lives=6):
        # Store the maximum number of lives and initialise the game state.
        self.max_lives = max_lives
        self.lives = max_lives
        self.secret_word = self.get_random_word()
        self.blanks = self.make_blanks(self.secret_word)
        self.used_letters = set()

    @staticmethod
    def get_random_word():
        # Keep the possible words inside the class so the game controls its own data.
        words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]
        return random.choice(words)

    @staticmethod
    def make_blanks(word):
        # Create one blank (_) for every letter in the secret word.
        return ["_" for _ in word]

    def prompt_for_letter(self):
        # Repeatedly ask for input until the player enters a valid, unused letter.
        while True:
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue

            if guess in self.used_letters:
                print(" → You already tried that letter.")
                continue

            return guess

    def reveal_letters(self, letter):
        # Reveal every occurrence of the guessed letter in the secret word.
        found_any = False

        for i, character in enumerate(self.secret_word):
            if character == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True

        return found_any

    def all_blanks_filled(self):
        # The player wins when there are no underscores left.
        return "_" not in self.blanks

    def display_game_state(self):
        # Display the current progress of the word to the player.
        print(" ".join(self.blanks))

    def play(self):
        # Control the main game loop.
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        self.display_game_state()

        while True:
            # Ask the player for a letter and remember it.
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            # Check whether the guessed letter appears in the secret word.
            if self.reveal_letters(guess):
                print("\n Well done, Nice job! You found a letter.")
                self.display_game_state()

                # Check whether all letters have been guessed.
                if self.all_blanks_filled():
                    print("\n Congratulations! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    break
            else:
                # Reduce the number of lives when the guess is incorrect.
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                self.display_game_state()

                # End the game when the player has no lives remaining.
                if self.lives <= 0:
                    print("\n Out of lives & Sad story!")
                    print(f"The word was: {self.secret_word}")
                    print("GAME OVER")
                    break


def main():
    # Create a game object and start the game.
    game = WordGuessingGame(max_lives=6)
    game.play()


if __name__ == "__main__":
    # Run main() only when this file is executed directly.
    main()
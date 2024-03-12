import random

class DragonCasino:
    def __init__(self):
        self.player_balance = 10000
        self.dragon_names = ['Firestorm', 'Nightshade', 'Thunderclap', 'Shadowfing']

    def display_menu(self):
        print("\nDragon Casino")
        print("1. Bet On A Dragon Race")
        print("2. Play Dragon Slots")
        print("3. Play Dragon Roulette")
        print("4. Check Balance")
        print("5. Quit")

    def bet_on_race(self):
        print("\nDragon Race Betting")
        print("Available Dragons:")
        for i, dragon in enumerate(self.dragon_names):
            print(f"{i+1}. {dragon}")

        selected_dragon = int(input("Choose Dragon You Want To Bet On (1-4): "))
        bet_amount = int(input("Enter your bet amount: "))

        if bet_amount > self.player_balance:
            print("Insufficient Balance!")
            return
        
        winning_dragon = random.choice(self.dragon_names)
        print(f"The Race Is Over! {winning_dragon} Won!")

        if selected_dragon == self.dragon_names.index(winning_dragon) + 1:
            winnings = bet_amount * 2
            print(f"Congratulations! You won {winnings}!")
            self.player_balance += winnings
        else:
            print("Better Luck Next Time!")
            self.player_balance -= bet_amount

    def play_slots(self):
        print("\nDragon Slots")
        print("You Pull The Lever Of The Dragon Slots...")
        slots = [random.choice(self.dragon_names) for _ in range(3)]
        print(" ".join(slots))
        if slots[0] == slots[1] == slots[2]:
            winnings = self.player_balance * 10
            print("Jackpot! All Dragons Matched!")
            print(f"You Won {winnings}!")
            self.player_balance += winnings
        else:
            print("No Luck This Time!")

    def play_roulette(self):
        print("\nDragon Roulette")
        bet_on = input("Choose your bet (even, odd, red, black, number): ").lower()
        if bet_on == "number":
            number = int(input("Enter the number you want to bet on (1-36): "))
            if 1 <= number <= 36:
                bet_amount = int(input("Enter your bet amount: "))
                if bet_amount <= self.player_balance:
                    result = random.randint(1, 36)
                    print(f"The Wheel Spins And Lands On {result}")
                    if result == number:
                        winnings = 36 * bet_amount
                        print("Congratulations! You Guessed The Right Number!")
                        print(f"You Won {winnings}!")
                        self.player_balance += winnings
                    else:
                        print("Better Luck Next Time!")
                        self.player_balance -= bet_amount
                else:
                    print("Insufficient Balance!")
            else:
                print("Invalid Number! Please Choose A Number Between 1-36.")
        elif bet_on in ["even", "odd", "black", "red"]:
            bet_amount = int(input("Enter your bet amount: "))
            if bet_amount <= self.player_balance:
                result = random.randint(0, 36)
                if ((bet_on == "even" and result % 2 == 0) or 
                    (bet_on == "odd" and result % 2 != 0) or 
                    (bet_on == "black" and result in range(1, 11) or result in range(20, 29)) or 
                    (bet_on == "red" and result in range(11, 20) or result in range(29, 36))):
                    print(f"The wheel spins and lands on {result}")
                    winnings = bet_amount * 2
                    print(f"Congratulations! You won {winnings}!")
                    self.player_balance += winnings
                else:
                    print("Better luck next time!")
                    self.player_balance -= bet_amount
            else:
                print("Insufficient Balance!")
        else:
            print("Invalid bet! Please choose from even, odd, black, red, or number.")

    def check_balance(self):
        print(f"Your Current Balance Is: {self.player_balance}")

    def play(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.bet_on_race()
            elif choice == '2':
                self.play_slots()
            elif choice == '3':
                self.play_roulette()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                print("Thanks for playing at Dragon Casino!")
                break
            else:
                print("Invalid choice! Please try again.")

# Main program
if __name__ == "__main__":
    casino = DragonCasino()
    casino.play()

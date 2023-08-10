import random
import streamlit as st

class NumberGuessGame:
    
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
    
        self.attempts = 0
        self.target = self.target_number()  # Generate the target number once
        
    def target_number(self):
        return random.randint(self.lower_bound, self.upper_bound)
    
    def play(self, user_guess):
        self.attempts += 1
        if user_guess < self.target:
            return f"Guess higher than {user_guess}"
        elif user_guess > self.target:
            return f"Guess lower than {user_guess}"
        else:
            return f"Congratulations! You guessed the number {user_guess}."

def main():
    st.title("Guess the Number Game")
    lower_bound = st.number_input("Enter lower bound:", value=1)
    upper_bound = st.number_input("Enter upper bound:", value=100)
    
    if 'game' not in st.session_state:
        st.session_state.game = NumberGuessGame(int(lower_bound), int(upper_bound))
    
    user_guess = st.number_input(f"Guess a number between {lower_bound} and {upper_bound}", min_value=lower_bound, max_value=upper_bound)
    message = ""

    if st.button("Check"):
        message = st.session_state.game.play(user_guess)
        # st.write(st.session_state.game.target)  # Display the fixed target number
    
    if st.button("Replay"):
        st.session_state.game = NumberGuessGame(int(lower_bound), int(upper_bound))
        message = "Game has been reset."

    st.write(message)
    st.write(f"Attempts: {st.session_state.game.attempts}")

if __name__ == "__main__":
    main()

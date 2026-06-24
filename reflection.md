# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The first time I ran the game, the secret number was 23. There were a total of 8 guesses. The UI included buttons that allowed guesses to be submmited, the game to be restarted, and a hint to be shown. 
- One bug I found was that it would incorrectly tell me to guess lower when I guessed 21 or 22. Another bug was that the reset game button would sometimes not do anything at all. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  21    | 📈 Go HIGHER!    |   📉 Go LOWER!   |     No error
|  25    | 📉 Go LOWER!     |   📈 Go HIGHER!  |    No error
| Newgame| Game resets      |   Does nothing   |      No error 

---

## 2. How did you use AI as a teammate?

- I used ChatGPT, Claude, and Codex during this project. I used them to help identify bugs, refactor code, generate tests, and review code changes before applying them.
- One correct suggestion was moving the game logic into logic_utils.py and fixing the string comparison bug. I verified it by running the game and checking that the hints worked correctly.
- One misleading suggestion passed the tests but still had the high/low messages reversed, which I caught by manually testing the game.

---

## 3. Debugging and testing your fixes

- I decided a bug was fixed only after testing it in the real game. One test I ran was checking that a guess of 60 against a secret number of 50 returned "Too High" and the message "Go LOWER!". I also tested a guess of 40 against a secret number of 50 and confirmed it returned "Too Low" and "Go HIGHER!".
- My AI also generated tests that checked the high and low hint behavior. These tests helped verify that the bug stayed fixed and that the logic was working correctly.

---

## 4. What did you learn about Streamlit and state?

- I learned that Streamlit reruns the entire script whenever a user interacts with the app, such as clicking a button or submitting a guess. Because of this, important information needs to be stored in st.session_state so it is not lost during reruns. In this project, session state was used to keep track of the secret number, attempts, score, and game status. Without the session state, the game would reset every time the page reran.

---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is testing fixes in the actual application instead of assuming they work. Running the game after making changes helped me catch issues that automated tests did not fully detect. If I never played the game myself and assumed the AI was always right, I would've never caught the bug again.
- Next time, I would manually test AI-generated fixes earlier in the process. I learned that even when AI-generated code looks correct and passes tests, there can still be problems in the actual application.
- This project showed me that AI agents can be really useful, but its suggestions should always be reviewed and verified. AI can help find bugs and write code quickly, but the developers/engineers are still responsible for testing and confirming that the code works correctly.

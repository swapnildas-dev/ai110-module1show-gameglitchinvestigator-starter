# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, I used the Developer Debug Info panel to compare my guesses against the secret number and the current session state. The first major bug I noticed was that the hint direction was backwards, so guesses above the secret could still tell me to go higher, and guesses below the secret could tell me to go lower. I also found that the New Game button could leave the app stuck after a game ended because the status was not reset to `"playing"`. While working through the fixes, I also cleaned up the logic by moving the helper functions into `logic_utils.py` so they could be tested more directly.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 21 | `📈 Go HIGHER!` | `📉 Go LOWER!` | No error |
| 25 | `📉 Go LOWER!` | `📈 Go HIGHER!` | No error |
| Click **New Game** after finishing a round | A fresh playable game starts | The app can remain stuck in a finished state | No error |

---

## 2. How did you use AI as a teammate?

I used ChatGPT, Claude, and Codex as debugging and review partners during this project. They were most helpful for spotting code smells, suggesting the refactor into `logic_utils.py`, generating tests, and showing diffs before applying changes. One especially useful suggestion was fixing the comparison logic so `check_guess` handled values numerically instead of relying on behavior that could produce the wrong hint direction. One flawed AI output still left the high/low hint messages reversed even though the tests passed at the time, which reminded me that AI suggestions still need manual verification in the actual app.

---

## 3. Debugging and testing your fixes

I treated a fix as complete only after checking both the app behavior and the automated tests. In the game itself, I confirmed that a guess of 60 against a secret of 50 returned `"Too High"` with `Go LOWER!`, and that a guess of 40 against 50 returned `"Too Low"` with `Go HIGHER!`. I also used pytest to validate the helper logic and ended with `7 passed` using `python -m pytest -q`. That combination of manual testing and automated tests helped me catch problems that either method alone might have missed.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the full script every time the user interacts with the page. Because of that, values like the secret number, attempts, score, history, and status need to live in `st.session_state` instead of regular local variables. This project made it clear that state bugs are not always about crashes; sometimes the app keeps running but behaves incorrectly across reruns. Resetting the game status during the New Game flow was a good example of how a small state mistake can break the user experience.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is asking for diffs before applying AI-generated changes and then testing those changes in the real app. Running the game after each fix helped me catch issues that were easy to miss in code review alone. Next time, I would manually test important user-facing behavior earlier instead of trusting a passing test suite too quickly. This project reinforced that AI can speed up debugging and refactoring, but I am still responsible for checking whether the final behavior is actually correct.

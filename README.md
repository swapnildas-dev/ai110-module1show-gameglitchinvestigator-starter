# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game Purpose

This project is a Streamlit number guessing game where the player tries to find a secret number within a limited number of attempts. The app tracks score, difficulty, guess history, and game status, and it also includes a debug panel that makes it easier to inspect state while debugging.

### Bugs Found

- The high/low hint direction was wrong. A guess above the secret could tell the player to go higher, and a guess below the secret could tell the player to go lower.
- Starting a new game did not reliably reset the game to a playable state because the status was not always set back to `"playing"`.
- The new-game flow recreated the secret number with a hardcoded `1-100` range instead of reusing the currently selected difficulty range.

### Fixes Applied

- Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` from `app.py` into `logic_utils.py`.
- Updated `app.py` to import the shared helpers from `logic_utils.py`.
- Fixed `check_guess` so it compares numerically and returns the correct hint direction:
  high guesses return `"Too High"` with a message to go lower, and low guesses return `"Too Low"` with a message to go higher.
- Fixed the new-game flow so it resets `st.session_state.status` to `"playing"` and generates the next secret number using the active difficulty range.
- Added and updated pytest coverage for win/high/low outcomes and helper-function behavior.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Launch the app with `python -m streamlit run app.py` and choose a difficulty from the sidebar.
2. Open **Developer Debug Info** to see the current secret number, attempt count, score, difficulty, and guess history while testing.
3. Enter a guess that is lower than the secret number and confirm the game returns `"Too Low"` with the hint `📈 Go HIGHER!`.
4. Enter a guess that is higher than the secret number and confirm the game returns `"Too High"` with the hint `📉 Go LOWER!`.
5. Enter the exact secret number and confirm the game shows the win state, balloons, and final score.
6. Click **New Game** and verify that the app starts a fresh round in the currently selected difficulty instead of staying stuck in a completed game state.

**Screenshot** *(optional)*: Not included in this write-up.

## 🧪 Test Results

```
$ python -m pytest -q
.......                                                                  [100%]
7 passed in 0.01s
```

## 🚀 Stretch Features

- No stretch features were added for this submission.

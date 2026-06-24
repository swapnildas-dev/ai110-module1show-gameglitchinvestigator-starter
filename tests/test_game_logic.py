from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_guess_numeric_string_secret_uses_numeric_comparison():
    outcome, _ = check_guess(9, "10")
    assert outcome == "Too Low"


def test_parse_guess_empty_input():
    assert parse_guess("") == (False, None, "Enter a guess.")


def test_get_range_for_difficulty_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_update_score_win():
    assert update_score(0, "Win", 1) == 80

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty

def test_hint_direction_guess_lower_than_secret():
    # Bug: guess=70, secret=98 showed "Go LOWER" instead of "Go HIGHER".
    # 70 < 98 means the guess is too low, so the player needs to go higher.
    outcome, message = check_guess(70, 98)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say Go HIGHER, got: {message}"

def test_easy_difficulty_range():
    # Bug: New Game button used randint(1, 100) regardless of difficulty,
    # so Easy could produce a secret like 43 which is outside 1-20.
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20, f"Easy should be 1-20, got {low}-{high}"

def test_normal_difficulty_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 50, f"Normal should be 1-50, got {low}-{high}"

def test_hard_difficulty_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 100, f"Hard should be 1-100, got {low}-{high}"

def test_string_comparison_bug_too_low():
    # Symmetric case: 19 < 20, so hint must be Too Low.
    # String comparison gives "19" > "20" == False correctly here,
    # but "9" > "20" == True, so 9 vs 20 is the edge case.
    outcome, _ = check_guess(9, 20)
    assert outcome == "Too Low"

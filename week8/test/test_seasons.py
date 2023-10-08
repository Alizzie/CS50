from datetime import date
from problems.seasons import calculate_difference, get_user_birthdate, sing_difference
import pytest

def test_calculate_difference():
    today = date.today()
    yesterday_day = today.day - 1
    yesterday = date(today.year, today.month, yesterday_day)
    assert calculate_difference(yesterday) == 1440

def test_get_user_birthdate_good():
    assert get_user_birthdate("1999-03-03") == date(1999, 3, 3)

def test_get_user_birthdate_bad():
    with pytest.raises(SystemExit):
        assert get_user_birthdate("January 1, 1999")

def test_sing_difference():
    assert sing_difference(1440) == "one thousand, four hundred and forty"
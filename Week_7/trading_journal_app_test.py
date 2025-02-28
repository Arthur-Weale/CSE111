import csv
import pytest
from trading_journal_app import calculate_win_rate, calculate_average_risk_reward

# Test calculate_win_rate with an empty CSV file (only header)
def test_calculate_win_rate_empty(tmp_path):
    csv_file = tmp_path / "tradelog.csv"
    header = "Trade Date,Instrument,Position,Entry Price,Exit Price,Stop Loss,Take Profit,Lot Size,Result,Status,Profit/Loss\n"
    csv_file.write_text(header)
    win_rate = calculate_win_rate(str(csv_file))
    assert win_rate == 0.0
    #  Check that the returned value is of type float.
    assert isinstance(win_rate, float)
    # Additional Assert 2: Check that win_rate is not negative.
    assert win_rate >= 0.0


# Test calculate_win_rate with one win and one loss (50% win rate)
def test_calculate_win_rate_basic(tmp_path):
    csv_file = tmp_path / "tradelog.csv"
    header = "Trade Date,Instrument,Position,Entry Price,Exit Price,Stop Loss,Take Profit,Lot Size,Result,Status,Profit/Loss\n"
    trade1 = "2025-01-01,XAUUSD,Long,2000,2020,1990,2050,1,Win,Saved,20\n"
    trade2 = "2025-01-02,XAUUSD,Long,2000,1980,1990,2050,1,Loss,Saved,-20\n"
    csv_file.write_text(header + trade1 + trade2)
    win_rate = calculate_win_rate(str(csv_file))
    assert win_rate == pytest.approx(50.0, rel=1e-2)
    assert win_rate <= 100.0
    assert win_rate > 0.0


# Test calculate_average_risk_reward with one win and one loss.
def test_calculate_average_risk_reward(tmp_path):
    csv_file = tmp_path / "tradelog.csv"
    header = "Trade Date,Instrument,Position,Entry Price,Exit Price,Stop Loss,Take Profit,Lot Size,Result,Status,Profit/Loss\n"
    trade1 = "2025-01-01,XAUUSD,Long,2000,2020,1990,2050,1,Win,Saved,20\n"
    trade2 = "2025-01-02,XAUUSD,Long,2000,1980,1990,2050,1,Loss,Saved,-10\n"
    csv_file.write_text(header + trade1 + trade2)
    average_rr = calculate_average_risk_reward(str(csv_file))
    # For one win (20 profit) and one loss (10 loss), average RR = 20/10 = 2.0
    assert average_rr == pytest.approx(2.0, rel=1e-2)
    assert isinstance(average_rr, float)
    assert average_rr > 0.0

pytest.main(["-v", "--tb=line", "-rN", __file__])

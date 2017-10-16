import datetime as dt
import decimal as dec

def calc_yield(open_date: dt.date, 
               base_cost: dec.Decimal,
               close_date: dt.date,
               closing_cost: dec.Decimal) -> dec.Decimal:
    duration: int = (close_date - open_date).days + 1 
    proceed: dec.Decimal = closing_cost - base_cost
    duration_relative: dec.Decimal = dec.Decimal(365/duration)

    return (proceed/base_cost) * duration_relative

def calc_yield_per_dollar_day(open_date: dt.date, 
               base_cost: dec.Decimal,
               close_date: dt.date,
               closing_cost: dec.Decimal) -> dec.Decimal:
    duration: int = (close_date - open_date).days + 1 
    proceed: dec.Decimal = closing_cost - base_cost
    total_dollars_days: dec.Decimal = duration * base_cost
    yield_per_dollar_day: dec.Decimal = proceed / total_dollars_days
    return yield_per_dollar_day * 365

print(calc_yield_per_dollar_day( dt.date(2017, 1, 1), 
    dec.Decimal("1000.1"),
    dt.date(2017,1, 30), 
    dec.Decimal("1100.2")))

print(calc_yield( dt.date(2017, 1, 1), 
    dec.Decimal("1000.1"),
    dt.date(2017,1, 30), 
    dec.Decimal("1100.2")))
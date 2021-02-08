"""A vaccination calculator."""

__author__ = "730246281"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent: int = int(input("Target percent vaccinated: "))

percent_target: float = target_percent / 100
already_vac: float = doses_admin / 2
pop_vac_per_day: float = doses_per_day / 2
un_vac: float = pop * percent_target
pop_needs_vac: float = un_vac - already_vac
days_until: int = round(pop_needs_vac / pop_vac_per_day)


today: datetime = datetime.today()
future_day: timedelta = timedelta(days_until)
vaccination_met: datetime = today + future_day


print("We will reach" + " " + str(target_percent) + "% vaccination in" + " " + str(days_until) + " " + "days, which falls on" + " " + (vaccination_met.strftime("%B %d, %Y")) + ".")

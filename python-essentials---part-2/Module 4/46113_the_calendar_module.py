"""
    Estimated time > 30-60 minutes
    Level of difficulty > Easy

    Objectives:
        Improving the student's skills in using the Calendar class.

    Scenario:
        During this course, we looked at the Calendar class a bit. Your task is to extend its functionality with a new
        method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number
         of occurrences of a specific weekday in the year.

    Use the following tips:
        Create a class called MyCalendar that extends the Calendar class;
        create the count_weekday_in_year method with the year and weekday parameters. The weekday parameter should be a
        value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
        in your implementation, use the monthdays2calendar method of the Calendar class.

    EXAMPLE 1:
        Sample arguments > year=2019, weekday=0
        Expected output > 52

    EXAMPLE 2:
        Sample arguments > year=2000, weekday=6
        Expected output > 53
"""
import calendar


class MyCalendar(calendar.Calendar):
    """
        Class to extend one more function to the calendar class
    """

    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self, year, weekday):
        '''
        Method to count how many specific weekdays exist in a year

        :param year: year counted
        :param weekday: specific weekday to count
        :return: int
        '''

        # Variable to count how many occurrences exists
        occurrences = 0

        # Checks if the weekday is valid
        if weekday in super().iterweekdays():

            # Iterate the months of a year
            for month in range(1, 13):

                # Iterate the days of the year
                for dayweek in super().monthdays2calendar(year=year, month=month):

                    # Iterate the results obtained only getting the values that are in that month
                    for day in filter(lambda x: x[0] != 0, dayweek):
                        if day[1] == weekday:
                            occurrences += 1

        return occurrences


# TESTING
obj = MyCalendar()

print(obj.count_weekday_in_year(year=2019, weekday=0))

print(obj.count_weekday_in_year(year=2000, weekday=6))

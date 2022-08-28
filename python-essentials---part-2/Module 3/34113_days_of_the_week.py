'''

Scenario

Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.

The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon).

The class should provide the following facilities:
    objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
    the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
    all object's properties should be private;

Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.

Expected output
    Mon
    Tue
    Sun
    Sorry, I can't serve your request.
'''


class WeekDayError(Exception):
    def __init__(self, value):
        if value not in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
            raise Exception('Error')


class Weeker(WeekDayError):
    #
    # Write code here.
    #

    def __init__(self, day):
        # Invoque the exception method to control if any error raise
        WeekDayError.__init__(self, day)

        # Saves the recived day
        self.day = day

        # Define all the existing days
        self.days_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __str__(self):
        return self.day

    # Function to change the add or subtract days from the week
    def __play_with_days(self, number_days, sum_or_subs):

        # Variable that gets the index of the current value
        current_index = self.days_of_the_week.index(self.day)

        # Iterates all the days recived
        for day in range(0, number_days):

            # Adds or subtract one more day to the current index
            current_index += 1 * sum_or_subs

            # Checks if the index is bigger than the length
            if current_index > len(self.days_of_the_week) - 1:

                # Resets the index to the minimun
                current_index = 0

            # Checks if the index is less than 0
            elif current_index < 0:

                # Sets the index to the last value of the index
                current_index = self.days_of_the_week.index(self.days_of_the_week[-1])

        return current_index

    # Function to add days to the weekday value
    def add_days(self, n):
        self.day = self.days_of_the_week[self.__play_with_days(n, 1)]

    # Function to subtract days to the weekday value
    def subtract_days(self, n):
        self.day = self.days_of_the_week[self.__play_with_days(n, -1)]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

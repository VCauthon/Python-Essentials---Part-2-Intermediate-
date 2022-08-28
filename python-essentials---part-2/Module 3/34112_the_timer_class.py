'''
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:
    objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
    the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.

Use the following hints:
    all object's properties should be private;
    consider writing a separate function (not method!) to format the time string.

Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

Expected output
23:59:59
00:00:00
23:59:59
'''


class Timer:

    def __init__(self, hours=0, minutes=0, seconds=0):
        # All the parameters are saved
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.__time_values = ["hours", "minutes", "seconds"]

    def __str__(self):
        # The returned variable is created
        time_in_string = ""

        # All the values inside the class are iterated
        for value in self.__dict__.keys():

            # Checks if the value iterated is from the timer
            if value in self.__time_values:

                # Creates the value to parse the data
                parse_value = ""

                # Check if the value iterated is lower than 10
                if self.__dict__[value] < 10:
                    # Adds one 0 at the beginning to represent the time value correctly
                    parse_value += "0"

                # Save the data to represent the results
                time_in_string += parse_value + str(self.__dict__[value])

                # Checks if the returned value needs to add one separator ":"
                if value != self.__time_values[-1]:
                    time_in_string += ":"

        return time_in_string

    def next_second(self):
        # Adds one second to the seconds variable
        self.seconds += 1
        self.__check_time()

    def prev_second(self):
        # Subtract one second to the seconds variable
        self.seconds -= 1
        self.__check_time()

    # Private function to refactor the timer with the current values
    def __check_time(self):

        # Creates a variable that save all the time values reversed
        time_reverser = self.__time_values[::-1]

        # Iterates all the values inside the timer variable reversed
        for time_value_cheked in time_reverser:

            # Checks if the value is greater than 59
            if self.__dict__[time_value_cheked] > 59:

                # Adds one value to the next time value and resets the current value
                self.__dict__[time_value_cheked] -= 60

                # Checks if the value iterated is not the hours one
                if time_value_cheked != self.__time_values[0]:
                    # Adds one value to the received one
                    self.__dict__[time_reverser[time_reverser.index(time_value_cheked) + 1]] += 1

            # Checks if the value is lesser than 0
            elif self.__dict__[time_value_cheked] < 0:

                # Adds one value to the next time value and resets the current value
                self.__dict__[time_value_cheked] = 59

                # Checks if the value iterated is not the hours one
                if time_value_cheked != self.__time_values[0]:
                    # Adds one value to the received one
                    self.__dict__[time_reverser[time_reverser.index(time_value_cheked) + 1]] -= 1

        # Checks if the hour is equals to 24
        if self.__dict__[self.__time_values[0]] == 24:

            for value in self.__time_values: self.__dict__[value] = 0

        # Checks if the hour is equals to 59 (it means that the hour have loop back)
        elif self.__dict__[self.__time_values[0]] == 59:

            self.__dict__[self.__time_values[0]] = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
timer.prev_second()
timer.prev_second()
timer.prev_second()
timer.prev_second()
timer.next_second()
timer.next_second()
timer.next_second()
timer.next_second()
timer.next_second()
timer.next_second()
timer.next_second()
timer.next_second()
print(timer)

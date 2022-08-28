"""
    Estimated time > 15-45 min
    Level of difficulty > Easy

    Objectives:
        improving the student's skills in date and time formatting;
        improving the student's skills in using the strftime method.

    Scenario:
        During this course, you learned about the strftime method, which requires knowledge of directives to create a format.
        It's time to put the known directives into practice.
        By the way, you'll have the opportunity to practice working with documentation, because you'll have to find directives that you don't yet know.

    Here's your task:
        Write a program that creates a datetime object for November 4, 2020 , 14:53:00.
        The object created should call the strftime method with the appropriate format to display the following result:
            2020/11/04 14:53:00
            20/November/04 14:53:00 PM
            Wed, 2020 Nov 04
            Wednesday, 2020 November 04
            Weekday: 3
            Day of the year: 309
            Week number of the year: 44

    Note: Each result line should be created by calling the strftime method with at least one directive in the format argument.
"""
from datetime import datetime

# Creation of the datetime object
date_used = datetime(2020, 11, 4, 14, 53, 00)

# Formating the date
print(date_used.strftime("%Y/%m/%d %H:%M:%S"))  # 2020/11/04 14:53:00
print(date_used.strftime("%y/%B/%d %H:%M:%S %p"))  # 20/November/04 14:53:00 PM
print(date_used.strftime("%a, %Y %b %d"))  # Wed, 2020 Nov 04
print(date_used.strftime("%A, %Y %B %d"))  # Wednesday, 2020 November 04
print(date_used.strftime("Weekday: %w"))  # Weekday: 3
print(date_used.strftime("Day of the year: %j"))  # Day of the year: 309
print(date_used.strftime("Week number of the year: %U"))  # Week number of the year: 44

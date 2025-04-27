from datetime import datetime, timedelta
from .models import *

from datetime import datetime, timedelta
import calendar  # Import the calendar module

def generate_weekdays(start_date_str, weekday, weeks):
    # Parse the start date
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    
    # Convert weekday string (e.g., "Monday") to an integer (e.g., 0 for Monday)
    weekday_index = list(calendar.day_name).index(weekday)

    # List to store the specified weekdays
    weekdays = []
    
    # Calculate the first occurrence of the specified weekday
    days_until_weekday = (weekday_index - start_date.weekday()) % 7
    first_weekday = start_date + timedelta(days=days_until_weekday)
    
    # Generate exactly one weekday per week
    for i in range(weeks):
        next_weekday = first_weekday + timedelta(weeks=i)
        weekdays.append(next_weekday.strftime("%Y-%m-%d"))  # Only the date part
    
    return weekdays

def create_classes(start_date_str, weekday, weeks, course_id, start_time, end_time):
    # Convert start_time and end_time strings to datetime.time objects
    start_time_obj = datetime.strptime(start_time, "%H:%M:%S").time()  # Assuming format is "HH:MM:SS"
    end_time_obj = datetime.strptime(end_time, "%H:%M:%S").time()      # Assuming format is "HH:MM:SS"

    # Generate the list of weekdays
    weekdays = generate_weekdays(start_date_str, weekday, weeks)
    
    for date_str in weekdays:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        class_instance = Class.objects.create(
            course_id=course_id,
            day=date_obj.strftime("%A"),  # Get the full weekday name
            start_time=start_time_obj,    # Use the converted time object
            end_time=end_time_obj,        # Use the converted time object
            date=date_obj.date()          # Store only the date part
        )
        class_instance.save()
    # Return the last created class instance for confirmation
    return class_instance
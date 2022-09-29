from icalendar import Calendar, Event, Alarm
import pytz
from datetime import datetime, timedelta
import os
import csv
from pathlib import Path


directory = str(Path(__file__).parent) + "/"
end_location_path = str(Path(__file__).parent) + "/ics_files/individual/"

# Create the calendar
cal = Calendar()
# cal.add('attendee', 'MAILTO:bradley@nteractive.com')
# cal.add('attendee', 'MAILTO:xyz@example.com')


description = """Thank you for registering for HPE Tech Next taking place on September 28, 2022.

We encourage you to look out for further emails from “HPE Tech Next”, containing additional information on the agenda, what to expect, and your unique Webinar join link. 

Best Regards
HPE Tech Next Team
"""
        
html_string= """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN"><HTML><BODY><p>Thank you for registering for HPE Tech Next taking place on September 28, 2022.
<br><br>
We encourage you to look out for further emails from “HPE Tech Next”, containing additional information on the agenda, what to expect, and your unique Webinar join link. 
<br><br>
Best Regards <br>
HPE Tech Next Team
</p></BODY></HTML>"""


# Create the event
event = Event()
event.add('summary', f'HPE Tech Next September 2022')
event.add('description', description)
event.add('X-ALT-DESC;FMTTYPE=text/html', html_string)
event.add('organizer', "enterprise.technology_summit@hpe.com")
event.add('location', "Zoom Webinar")
event.add('dtstart', datetime(2022, 9, 28, 13, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2022, 9, 28, 16, 0, 0, tzinfo=pytz.utc))
# event.add('alarm', datetime(2022, 4, 13, 11, 0, 0, tzinfo=pytz.utc))
# event.add('dtstamp', datetime(2021, 11, 4, 0, 10, 0, tzinfo=pytz.utc))
reminderMins = 15
alarm = Alarm()
alarm.add("action", "DISPLAY")
alarm.add('description', "Reminder")
alarm.add("trigger", timedelta(minutes=-reminderMins))
# The only way to convince Outlook to do it correctly
alarm.add("TRIGGER;RELATED=START", "-PT{0}M".format(reminderMins))
event.add_component(alarm)

# Adding events to calendar
cal.add_component(event)

f = open(os.path.join(end_location_path, f' HPE Tech Next September 2022.ics'), 'wb')
f.write(cal.to_ical())
f.close()

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


description = """Thank you for registering to attend the VMware Executive Summit.
Monday 7 November it will take place at the Esferic Barcelona, Plaça Dante. Montjuïc - Jardins Joan Brossa, 08038 Barcelona
Tuesday 8 November it will take place at the Fira Barcelona Gran Via, Carrer del Foc 10, 08038 Barcelona
 
To view the latest up-to-date information about the Executive Summit, please go to https://www.vmware.com/explore/executive-summit/eu.html.
 
We look forward to welcoming you in Barcelona, 7-8 November.

Your VMware Executive Summit Team
VMwareExecutiveEvents@Nteractive.com"""
        
html_string= """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN"><HTML><BODY><p>Thank you for registering to attend the VMware Executive Summit.
 <br><br>
Monday 7 November it will take place at the Esferic Barcelona, Plaça Dante. Montjuïc - Jardins Joan Brossa, 08038 Barcelona<br>
Tuesday 8 November it will take place at the Fira Barcelona Gran Via, Carrer del Foc 10, 08038 Barcelona
 <br><br>
To view the latest up-to-date information about the Executive Summit, please <a href="https://www.vmware.com/explore/executive-summit/eu.html">click here</a>.
 <br><br>
We look forward to welcoming you in Barcelona, 7-8 November.
 <br><br>
Your VMware Executive Summit Team<br>
<a href="mailto:VMwareExecutiveEvents@Nteractive.com">VMwareExecutiveEvents@Nteractive.com</a></p></BODY></HTML>"""


# Create the event
event = Event()
event.add('summary', f'Executive Summit at VMware Explore 2022')
event.add('description', description)
event.add('X-ALT-DESC;FMTTYPE=text/html', html_string)
event.add('organizer', "VMwareExecutiveEvents@Nteractive.com")
event.add('location', "Barcelona, Spain")
event.add('dtstart', datetime(2022, 11, 7, 9, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2022, 11, 8, 17, 0, 0, tzinfo=pytz.utc))
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

f = open(os.path.join(end_location_path, f' Executive Summit at VMware Explore 2022.ics'), 'wb')
f.write(cal.to_ical())
f.close()

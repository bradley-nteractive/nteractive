from icalendar import Calendar, Event
import pytz
from datetime import datetime, timedelta
from dateutil.parser import parse
import os
import csv
from pathlib import Path

# w_dir = os.path.dirname(os.path.abspath(__file__))
# print(w_dir)
directory = str(Path(__file__).parent) + "/"
end_location_path = str(Path(__file__).parent) + "/ics_files/"
fifteen_minutes = timedelta(minutes=15)
one_hour = timedelta(minutes=60)
prev_session_code = None
session_url = "https://reg.rainfocus.com/flow/hpenterprises/tss22/catalogembed/page/catalog/session/"

# Read the CSV
with open(directory + 'Session Links for Cal Blockers.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    for row in csv_reader:
        
        # Get data from csv row
        title = row['TITLE']
        titleClean = row['TITLE'].replace("/", " ").replace(":", "-").replace("?", "").replace("|", "-").replace("+", "&")
        date = row['DATE']
        first_key = list(row.keys())[0]
        id = row[first_key]
        file_id = id
        if id == prev_session_code:
            file_id = id + "_r"
            prev_session_code = file_id
        elif prev_session_code == id+"_r":
            file_id = id + "_r2"
            prev_session_code = file_id
        else:
            prev_session_code = id
        session_id = row['SESSION ID']
        email = row['EMAIL'].split(',')
        print(email)
        session_link = session_url + session_id
        lobby_link = "https://reg.rainfocus.com/flow/hpenterprises/tss22/lobby/page/portal"
        if date:
            print(date)
            date_repl = date.replace('/','-')
            date_split = date_repl.split('-')
            print(session_id, date_split)
            day = int(date_split[1])
            month = int(date_split[0])
        start_time = date + " " + row['TIME']
        end_time = date + " " + row['END TIME']
        parsed_start = parse(start_time)
        start_time_formatted = datetime.strptime(start_time,"%d/%m/%Y %H:%M") - fifteen_minutes - one_hour
        end_time_formatted = datetime.strptime(end_time,"%d/%m/%Y %H:%M") - one_hour
        description = """Please ensure you accept this calendar blocker invitation as it contains a deep link to your HPE TSS 2022 session on the event platform. \n
On the date and time of your session, click on this deep link: {vars} \n
Please note:
    - You need to be registered to access your sessions. If you haven’t already, please register here: https://reg.rainfocus.com/flow/hpenterprises/tss22/singleflowreg
    - You need to already be logged into the event platform to access your session directly from the deep link. Alternatively, go to the “My Agenda” tab from the lobby (https://reg.rainfocus.com/flow/hpenterprises/tss22/lobby/page/portal), find the Session you wish to join and then click “Join Webinar” (NB: links will appear 15 minutes before the session is due to start)
    - You should visit the Speaker Task list and complete the mandatory speaker tasks before your session.  To do this log into the lobby and click on the 'Task List' icon in the top right hand corner of your screen 

In case of any questions, please email hpetsscontent@nteractive.com.

Kind Regards,
HPE TSS 2022 Speaker & Content Team""".format(vars=session_link)
        html_string= """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN"><HTML><BODY><p>Please ensure you accept this calendar blocker invitation as it contains a deep link to your HPE TSS 2022 session on the event platform. <br><br>
On the date and time of your session, click on this <a href="{session_link}">deep link</a>.<br><br>
Please note <ul>
    <li> You need to be registered to access your sessions. If you haven’t already, please <a href="https://reg.rainfocus.com/flow/hpenterprises/tss22/singleflowreg">register here</a></li>
    <li>You need to already be logged into the event platform to access your session directly from the deep link. Alternatively, go to the “My Agenda” tab from the <a href="https://reg.rainfocus.com/flow/hpenterprises/tss22/lobby/page/portal">lobby</a>, find the Session you wish to join and then click “Join Webinar” (NB: links will appear 15 minutes before the session is due to start)</li>
    <li> You should visit the Speaker Task list and complete the mandatory speaker tasks before your session.  To do this log into the <a href="https://reg.rainfocus.com/flow/hpenterprises/tss22/lobby/page/portal">lobby</a> and click on the 'Task List' icon in the top right hand corner of your screen</li>
</ul>
In case of any questions, please <a href="mailto:hpetsscontent@nteractive.com">contact us</a>. <br><br>

Kind Regards,<br>
HPE TSS 2022 Content Team </p></BODY></HTML>""".format(session_link=session_link)

        # Create the calendar
        cal = Calendar()

        

        # Create the event
        event = Event()
        event.add('summary', f'HPE TSS Speaker | {id} - {title}')
        event.add('description', description)
        event.add('X-ALT-DESC;FMTTYPE=text/html', html_string)
        event.add('dtstart', start_time_formatted)
        event.add('dtend', end_time_formatted)
        event.add('dtstamp', start_time_formatted)
        event.add('location', session_link)
        # event.add('attendee', "bradley.nteractive@gmail.com")

        for e in email:
            print(e)
            # event.add("ATTENDEE;ROLE=REQ-PARTICIPANT;", e)
            event.add('attendee', e)

        # Adding events to calendar
        cal.add_component(event)

        f = open(os.path.join(end_location_path, f'{file_id} - {titleClean}.ics'), 'wb')
        f.write(cal.to_ical())
        f.close()



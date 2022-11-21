# nteractive

## ICSatron
**Installation**
1. Install Python to your machine (from the Windows store if on PC)
2. Using VScode, or your editor of choice, add the ics files to your editor, then in a terminal window install dependencies with `pip install -r requirements.txt`. Pip should be installed as part of the Python package.
3. There are two script files in the folder - 
  1. Use individual ICS files to create a single ics file using the parameters outlined
  2. Use the ics_atron2000.py script to create all ics files, using a csv report added to the root folder (ics_generator_master)

**Config**
1. Select the script file required - either bulk or individual, then update the `description`, `html_string` variables with the calendar invite content. These variables provide a html and plain text string, to ensure compatability.
2. On the bulk script, the start time / end time is set using the session time in the CSV file. As per HPEs request, the actual time blocked on the calendar is 15mins prior to the actual session start time. To account for timezones, since the RainFocus CSV data is on CET, but the ICS is sent from GMT, the `start_time_formatted` (line 54) takes the CSV start time, removes 15 minutes so it's blocked early, then removes another hour to account for timezones. If you need to create the ICS files with the same timezone as the CSV or start at the actuall time, the `- fifteen_minutes` or `- one_hour` can be removed from this variable.
3. Line 95 will add each speaker / participant email to the 'to' section in the ICS file (from the CSV data). If this is not required, comment out line 95 - 98.
4. When config is complete, hit the 'run script' button to generate the files. All files will then be saved in '/ics_files/' in the root of the project.

'''#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY. '''
import shutil, os, re

# Create a regex that matches the MM-DD-YYYY date format
datePattern = re.compile(r"""^(.*?)         # all text before the date
                        ((0|1)?\d)-         # one or two digits for the month
                        ((0|1|2|3)?\d)-     # one or two digits for the day
                        ((19|20?\d\d))      # four digits for the year
                        (.*?)$              # all text after the dste
                        """, re.VERBOSE)

# Loop over files in the working directory
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)          

# Skip file without a date
    if mo == None:
        continue

# Get different part of the file name
    #beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8) 

# form the DD-MM-YY date format
euroFilename = dayPart + '-' + monthPart + '-' + yearPart + afterPart

# get the full absolute file path
absWorkingDir = os.path.abspath('.')
amerFileName = os.path.join(absWorkingDir, amerFileName)
euroFilename = os.path.join(absWorkingDir, amerFileName)

# rename the files
print(f'Renaming "{amerFileName}" to "{euroFilename}".....')
#shutil.move(amerFileName,euroFilename) 



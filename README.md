# Date-format-file-rename

Here’s what the program does:
1. It searches all the filenames in the current working directory for
American-style dates.
2. When one is found, it renames the file with the month and day
swapped to make it European-style.
This means the code will need to do the following:
1. Create a regex that can identify the text pattern of American-style dates.
2. Call os.listdir() to find all the files in the working directory.
3. Loop over each filename, using the regex to check whether it has a date.
4. If it has a date, rename the file with shutil.move().

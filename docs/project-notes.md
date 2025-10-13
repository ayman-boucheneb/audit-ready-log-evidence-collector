# Notes taken during the project

1. FileNotFoundError - occurs when a file or directory doesn't exist. Ended up using the example provided by Real Python(2025) and applied it to my code in parse.py

2. Creating a CSV File using Python - done by importing the 'csv' module and defining its path & data, helped me establish the file 'alerts.csv' if there was no such file created yet.

3. Creating a new folder =  You import the 'os' module and use os.mkdir() method to create the folder. This method and the example provided by freeCodeCamp.org (2023), where they used the try/except method to create the new folder if it doesn't exist, was applied to my code.

4. Parsing logs - Done by importing the 're' module and providing a log_pattern (GeeksforGeeks, 2024). I did unfortunetly struggle to apply this because this was a new concept for me, especially the log patterns that need to be applied because they have complicated signs to be defined. 
The ChatGPT chat that provided instructions like a unicersity course did apply the log patterns for me and gave me extra hints such as ".writeheader()" & "csv.dictWriter" methods. I did try my best to use these hints to write up the code, which was executed but not as efficiently.

5. My initial code resulted in summary.csv have one line containing a series of red boxes saying "ERROR" on them. This is because my code didn't take into account lines that may not match the log pattern, meaning the line cannot be parsed properly. ChatGPT helped fix this by using multiple if statements, which I tried to apply to my code that was partially working already (ChatGPT, 2015). Another implementation was the match() function, which validates whether a non-empty line matches the log pattern assigned in the code.

6. Counter() class was used to create counters for iterable objects (GeeksforGeeks, 2024). In my code, I used it to count the most common IPs, status codes, and paths found in the log file. It was also used for rule-specific checks, such as counting how many times sensitive paths were accessed and how many failed authentication attempts occurred (status 401 meant unauthorized, or 403 which meant forbidden). The any() function was used to check if any of the conditions in the sensitive paths list were true for a given log line, which made the detection cleaner and easier instead of writing multiple if statements (www.w3schools.com, n.d.).





## References:
1. Real Python (2025). FileNotFoundError | Python’s Built-in Exceptions – Real Python. [online] Realpython.com. Available at: https://realpython.com/ref/builtin-exceptions/filenotfounderror/ [Accessed 28 Sep. 2025].
2. GeeksforGeeks (2024). How To Create A Csv File Using Python. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/how-to-create-a-csv-file-using-python/ [Accessed 28 Sep. 2025].
3. freeCodeCamp.org. (2023). Creating a Directory in Python – How to Create a Folder. [online] Available at: https://www.freecodecamp.org/news/creating-a-directory-in-python-how-to-create-a-folder/ [Accessed 28 Sep. 2025].
4. GeeksforGeeks (2024) Parse and Clean Log Files in Python, GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/parse-and-clean-log-files-in-python/ [Accessed 28 Sep. 2025].
5. ChatGPT. (2015). ChatGPT - CSV file issues. [online] Available at: https://chatgpt.com/share/68e8d2b1-27ac-800b-8e73-f089f06315b5 [Accessed 28 Sep. 2025].
6. GeeksforGeeks (2018). Python | Counter Objects | elements(). [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python/python-counter-objects-elements/ [Accessed 10 Oct. 2025].
7. www.w3schools.com. (n.d.). Python any() Function. [online] Available at: https://www.w3schools.com/python/ref_func_any.asp [Accessed 10 Oct. 2025].
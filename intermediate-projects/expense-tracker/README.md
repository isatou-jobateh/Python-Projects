# DalasiTrack 

DalasiTrack is a text-based expense tracker I built using Python. I wanted to work on something practical while practising the Python concepts I had learned, rather than just writing small exercises.

The program uses Gambian dalasi (D) and lets users record expenses, check their total spending, see where their money goes by category, set a budget, and search for particular expenses. It can also save expenses to a text file so they are available when the program is opened again.

## 1. The Problem I Wanted to Solve

I wanted to make it easier to keep track of everyday spending. It can be difficult to know how much money has gone out or which things take up most of a budget when expenses are not recorded in one place.

I decided to build a simple tool that could organise expenses and show useful spending information without making the process complicated.

## 2. Who Experiences This Problem and Why It Matters

This is something that can affect anyone managing their own money, including students, households, and people working with a limited budget.

Keeping track of expenses can help people understand their spending habits, plan their budgets, and make better decisions about how they use their money. I also wanted the project to feel relevant to my own environment, so I used Gambian dalasi as the currency.

## 3. What I Researched and Which Alternatives I Considered

While building DalasiTrack, I worked on how to organise expense information, calculate totals, group expenses by category, and store records in a file.

I used a list of dictionaries to keep each expense's name, category, and amount together. For storage, I chose a plain text file with one expense per line instead of introducing a database or a more advanced data format.

I kept the project text-based rather than starting with a graphical interface. This allowed me to concentrate on the program's logic and practise the Python concepts I had learned.

## 4. Why I Chose This Solution

I chose this project because it combines a practical everyday problem with an opportunity to practise Python in one program.

While developing it, I used lists, dictionaries, loops, conditional statements, comprehensions, lambda expressions, calculations, and file handling. I also worked with file paths while fixing an issue with where expenses were being saved.

Building the program this way helped me understand how different Python concepts work together in a larger project.

## 5. How I Tested It, What Happened, and Bugs I Fixed

I started the program with three sample expenses: CashPower, rice, and cooking gas. I then tested the menu options for adding and viewing expenses, calculating total spending, checking category totals, finding the largest expense, setting a budget, searching, filtering, and saving records.

During testing, I encountered a few bugs that I had to investigate and fix.

### Bug 1: Spending by category showed incorrect totals

At first, the category summary was not adding the expense amounts together correctly. I reviewed the calculation and fixed it so that each expense amount was added to the running total for its category. After the change, the program displayed the correct totals for categories such as Electricity, Food Staples, and Utility.

### Bug 2: Expenses were being saved to different files

I noticed that two files named `expenses.txt` had been created in different locations. I checked the working directory printed by Python and compared it with the location of my Python script.

I discovered that the program was using a relative file path, which meant it could save the file in a different directory depending on where it was run. I fixed this by using `os.path` to build the path relative to `dalasitrack.py`, so the program would use the intended file beside the script.

### Bug 3: New expenses replaced previously saved expenses

After adding expenses on separate runs, I noticed that an earlier expense could disappear from the saved records. The program was saving the current in-memory list, but it was not loading the previously saved expenses when it started.

I worked on the file-loading logic so that the program could read the existing records before accepting new expenses. I tested the change by saving the expenses, restarting the program, and viewing the records again. All six expenses appeared after restarting, confirming that the persistence test passed.

### Testing results

After making these fixes, I checked the category summary and tested saving and loading expenses across program restarts. The program correctly retained all six expenses in my final persistence test.

These issues helped me understand that a program can appear to work during one session but still have problems with calculations, file paths, or data persistence. Testing and investigating those problems were important parts of completing the project.

## 6. What I Would Improve or Do Differently Next Time

If I continued developing DalasiTrack, I would improve how it handles invalid menu choices and non-numeric input, so unexpected entries do not interrupt the program.

I would also consider adding monthly spending summaries, comparing spending across different periods, and making it easier to manage expenses over time.

This project taught me that building software is not only about writing code. It also involves testing, debugging, checking assumptions, and making improvements when something does not behave as expected.

## Technologies Used

* Python
* Lists and dictionaries
* Loops and conditional statements
* List comprehensions and lambda expressions
* File handling
* `os.path` for file paths

## Project Status

**Completed:** Initial text-based prototype and persistence testing.

DalasiTrack is part of my Python learning portfolio, where I practise applying what I learn to practical projects.

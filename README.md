# Salary calculation for employees in ACME Company
## Considerations

I took the following considerations for my solution:
- The raw string will always have the name of the employee and the equals sign
- Format time is in 24 hours format, but the 24th hour is represented as 0
- The employees schedules will have to be bounded in the three schedules of the day, for example 08:00-14:00 will not be valid
- We only consider the hours part to calculate the salary, not the minutes
- The input file exists and its called input.txt

## Overview of the solution
The solution is divided in three parts, the first is the **init** function that is in charge of reading the *input.txt* file. Then for each employee schedule it calls the **validateSchedule(schedules)** function to validate its format, if it's correct then proceeds to call the **calculateSalary(schedule)** function to calculate the salary using a dictionary of salaries predefined. If the validation fails then the program prints an error message and continues the execution with the next employee schedule for the same process.

## Methodology
After reading the exercise two times, I though I would need an object-oriented solution for the employees and a library for the time management, but I figured out that a class of employees would cause a **code smell** of lazy class because of the lack of responsabilities. Then I realized I couldn't use any external library such as time. So, I read carefully the input structure of the examples which had the name of the employee separated by an equals sign and the schedules were separated by commas, hence I decided to use string slicing to extract that information. 

After that, I planned some paths to solve the problem with the general idea of having a main function which calls a function to validate the schedules format and a function for calculating the salary. Therefore, I solved the problem by programming it without any considerations in good programming practices. At that point, my job was to review the code and make it more readable and efficient. Later I got rid of many nested-if statements and changed the name of some variables for intuitive names. 

In the end, I programmed the unit tests for both functions and I realized that there was a problem when the end hour of a schedule is 0. I considered it as a special case. so my solution was to do a validation using a ternary expression which is if the value in the end hour is 0, then change it to 24. And it was done.

## Good programming practices
- Variables and functions have an specified convention which is camelcase
- Variables and function names are intuitive depending on its purpose in the program
- Single-Responsability Principle for validate and calculate functions
- Unit tests were made for only possible cases in the program
- Just enough comments to understand the code
- Divide and conquer design paradigm
- Constants are in uppercase

## Run the program
First of all, the Python version is "3.7.9". This program uses the library **unittest** which is a built-in library for unit testing, so you don't need to install any dependency via **pip**.
1) Unzip the Ejercicio_ACME.zip
2) Open a console in the folder of the project
3) Type "python main.py" to run the program
4) Type "python test_main.py" to run program and the unit tests
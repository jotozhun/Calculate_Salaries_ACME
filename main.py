DAYS_OF_WEEK = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
DAYS = DAYS_OF_WEEK[0:5]
WEEKEND = DAYS_OF_WEEK[5:7]

SALARY_BY_SCHEDULE = {
    "day": [
        {"start": 0, "end": 9, "earn": 25},
        {"start": 9, "end": 18, "earn": 15},
        {"start": 18, "end": 24, "earn": 20}
    ],
    "weekend": [
        {"start": 0, "end": 9, "earn": 30},
        {"start": 9, "end": 18, "earn": 20},
        {"start": 18, "end": 24, "earn": 25}
    ]
}

def calculateSalary(schedules):
    earning = 0
    for schedule in schedules:
        day = schedule[0:2]
        startHour = int(schedule[2:4])
        endHour = 24 if schedule[8:10] == "00" else int(schedule[8:10]) # It's an special case when time is 24 hours, but the input is 0
        typeOfDay = "day" if day in DAYS else "weekend"

        for scheduleSalary in SALARY_BY_SCHEDULE[typeOfDay]:
            isBetweenSchedule = startHour >= scheduleSalary["start"] and endHour <= scheduleSalary["end"]
            if isBetweenSchedule:
                earn = (endHour - startHour) * scheduleSalary["earn"]
                earning += earn
    
    return earning


def validateSchedule(schedules):
    isScheduleValid = True
    for schedule in schedules:
        isFormatValid = len(schedule) == 13 and schedule[0:2] in DAYS_OF_WEEK and schedule[2:4].isdigit() and schedule[8:10].isdigit() and int(schedule[2:4]) < (24 if schedule[8:10] == "00" else int(schedule[8:10]))
        if not isFormatValid:
            isScheduleValid = False
    return isScheduleValid


def init():
    employees = open("input.txt", "r")
    for employee in employees.read().splitlines():  # read().splitlines() returns a list and gets rid of \n of every element
        schedule = employee.split("=")
        name = schedule[0]
        schedules = schedule[1].split(",")
        if validateSchedule(schedules):
            salary = calculateSalary(schedules)
            print(f"Input\n{employee}\nOutput\nThe amount to pay {name} is: {salary} USD\n")
        else:
            print("Format of Schedule is not valid, please try again!")

    employees.close()

init()
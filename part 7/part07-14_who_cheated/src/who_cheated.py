# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    start_times = {}
    with open('start_times.csv') as start_file:
        start_reader = csv.reader(start_file, delimiter=';')
        for row in start_reader:
            name, start_time = row
            start_times[name] = datetime.strptime(start_time, '%H:%M')

    cheater = []
    with open('submissions.csv', 'r') as submissions_file:
        submissions_reader = csv.reader(submissions_file, delimiter=';')
        for row in submissions_reader:
            name, task, points, submission_time = row
            submission_time = datetime.strptime(submission_time, '%H:%M')

            if name in start_times:
                time = start_times[name] + timedelta(hours=3)
                if submission_time > time:
                    if name not in cheater:
                        cheater.append(name)

    return cheater
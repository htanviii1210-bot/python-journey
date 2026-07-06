def average(marks):
    return round(sum(marks)/len(marks), 2)

def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)

def passed_students(marks):
    return [mark for mark in marks if mark >= 40]

def failed_students(marks):
    return [mark for mark in marks if mark < 40]

def distinction_students(marks):
    return [mark for mark in marks if mark > 85]





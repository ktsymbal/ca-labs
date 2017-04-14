from terminaltables import AsciiTable


def error(error_message):
    print(error_message, '\n')


def menu():
    print('\n[1] BMR Calculator(Basal Metabolic Rate Calculator)')
    print('[2] Daily Calorie Calculator')
    print('[3] BMI Calculator(Body Mass Index Calculator)')
    print('[4] View all')
    print('[5] Quit')
    try:
        choice = int(input('Your choice: '))
        if not 1 <= choice <= 6:
            raise ValueError
        return choice
    except ValueError:
        error('Invalid input')
        return None


def sex_input():
    try:
        sex = input('Enter your sex ("male" / "female"): ')
        if not sex in ('male', 'female'):
            raise ValueError
        return sex
    except ValueError:
        error('Invalid input')
        return None


def age_input():
    try:
        age = int(input('Enter your age (in years): '))
        if age <= 0:
            raise ValueError
        return age
    except ValueError:
        error('Invalid input')
        return None


def weight_input():
    try:
        weight = float(input('Enter your weight(in kilograms): '))
        if weight <= 0:
            raise ValueError
        return weight
    except ValueError:
        error('Invalid input')
        return None


def height_input():
    try:
        height = float(input('Enter your height(in centimeters): '))
        if height <= 0:
            raise ValueError
        return height
    except ValueError:
        error('Invalid input')
        return None


def exercise_level_input():
    try:
        exercise_level = input('Enter exercise level ("None"/"Sedentary"/"Light"/"Moderate"/"Hard"/"Non-Stop"): ')
    except ValueError:
        error('Invalid input')
        return None
    return exercise_level


def data_output(sex, age, weight, height):
    table_data = [
        ['SEX', 'AGE', 'WEIGHT', 'HEIGHT'],
        [sex, age, weight, height]
    ]
    table = AsciiTable(table_data, 'PHYSIQUE')
    print('\n', table.table)


def bmi_data_output(weight, height, bmi):
    table_data = [
        ['WEIGHT', 'HEIGHT', 'BMI'],
        [weight, height, bmi]
    ]
    table = AsciiTable(table_data, 'Body Mass Index Calculator')
    print('\n', table.table)


def daily_data_output(sex, age, weight, height, exercise_level, daily_rate):
    table_data = [
        ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'EXERCISE LEVEL', 'DAILY RATE'],
        [sex, age, weight, height, exercise_level, daily_rate]
    ]
    table = AsciiTable(table_data, 'Daily Calorie Calculator')
    print('\n', table.table)


def bmr_data_output(sex, weight, height, age, bmr):
    table_data = [
        ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'BMR'],
        [sex, age, weight, height, bmr]
    ]
    table = AsciiTable(table_data, 'Basal Metabolic Rate Calculator')
    print('\n', table.table)


def full_output(sex, age, weight, height, exercise_level, daily_rate, bmr, bmi):
    table_data = [
        ['SEX', 'AGE', 'WEIGHT', 'HEIGHT', 'EXERCISE LEVEL', 'DAILY RATE', 'BMR', 'BMI'],
        [sex, age, weight, height, exercise_level, daily_rate, bmr, bmi]
    ]
    table = AsciiTable(table_data, 'Full Calculations')
    print('\n', table.table)

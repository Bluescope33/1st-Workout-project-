
# User their goal
# Available equipment
# How many days per week they can train
# How many minutes per day
# Difficulty level
# Genertate a workout plan based on all
# Display the workout plan
# Ask if they want to log reps
# If yes, store their reps in a file

from pkgutil import get_data


def get_user_goal():

    # ask for goal how many days a week, mintues per week
    print = ("Hello and welcome to my 1st project")
    goal = input("What's your fitness goal? (strength, fat loss, muscle gain)")
    days = int(input("How many days a week do you have to workout?"))
    minutes = int(input("How long do you have to workout per-workout?"))
    level_of_diffictly = input(
        "What difficutly level are you looking for? (beginner / intermediate / advanced)")
    user_data = {goal: goal, days: days, minutes: minutes,
                 level_of_diffictly: level_of_diffictly}

    # return all goals
    return user_data


def get_user_equipment():

    # ask for user avaliable equitment
    equipment = input(
        "What equipment do you have avaliable to you? (no_equipment, dumbbells, full_gym)")
    avaliable_equipment = {equipment: equipment}
    # retrun all equipment
    return equipment


def give_user_workout_plan():

    # generate user workout plan
    import workout_data
    print = ("User {workout_data} + {level_of_diffictly}")


def user_progess():
    pass
    level_of_diffictly = "easy", "medium", "hard"

    # save user reps, difficulty to the JSON file

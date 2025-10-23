
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
import workout_logic
import datetime
import json


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
    available_equipment = {equipment: equipment}
    # return all equipment
    user_data = equipment
    return user_data

    import workout_data


def give_user_workout_plan(strength_exercises, fat_loss_exercises, core_exercises):
    # generate user workout plan
    print(f"Workout strength plan: {strength_exercises}")
    print(f"Workout fat loss plan: {fat_loss_exercises}")
    print(f"Workout core plan: {core_exercises}")


def user_progress():
    # log user progress
    level_of_difficulty = "easy", "medium", "hard"
    user_reps = input(
        "Please rate the level of difficulty of today's workout (easy, medium, hard): ")
    if user_reps not in level_of_difficulty:
        print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")


def handle_difficulty(level_of_difficulty):
    import workout_logic  # make sure this file exists in the same folder

    if level_of_difficulty == "hard":
        user_adjust = input(
            "This workout is hard. Would you like to adjust it? (yes/no): ").lower()

        if user_adjust == "yes":
            workout_logic.adjust_for_difficulty()
        elif user_adjust == "no":
            workout_logic.keep_same_difficulty()
        else:
            print("Invalid choice. Keeping the same difficulty.")

    # save user reps, difficulty to the JSON file

    # Load existing logs
    with open("workout_logs.json", "r") as f:
        logs = json.load(f)

    # Create a new entry with today's date
    new_entry = {
        "date": datetime.date.today().isoformat(),
        "goal": "strength",
        "equipment": "dumbbells",
        "workouts": ["push-ups", "Squats", "Planks"],
        "reps": {"Push-ups": 20, "Squats": 30, "Planks": "30 sec"},
        "difficulty": "medium"
    }

    # Add the new entry
    logs.append(new_entry)

    # Save back to JSON
    with open("workout_logs.json", "w") as f:
        json.dump(logs, f, indent=4)
    # Save back to JSON
    with open("workout_logs.json", "w") as f:
        json.dump(logs, f, indent=4)

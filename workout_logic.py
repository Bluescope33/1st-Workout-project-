# apps brain

<<<<<<< HEAD
def generate_plan(goal, equipment, days, minutes, difficulty):
    # decides which exercises to use based on users chocies
    pass
=======
import workout_data


def generate_plan(goal, equipment, days, minutes, difficulty):
    # decides which exercises to use based on users chocies
    if goal == "strength":
        exercises = workout_data.strength_exercises.get(
            equipment, [days, minutes, difficulty])
    elif goal == "fat loss":
        exercises = workout_data.fat_loss_exercises.get(
            equipment, [days, minutes, difficulty])
    elif goal == "core":
        exercises = workout_data.core_exercises.get(
            equipment, [days, minutes, difficulty])

    if days < 5:  # if user wants to work out less than 5 days a week
        exercises = exercises[:3]  # limit to 3 exercises per day
    if minutes < 30:  # if user wants to work out less than 30 minutes
        exercises = exercises[:2]  # limit to 2 exercises per day

    return exercises
>>>>>>> 558d384 (Initial project setup)


def adjust_for_difficulty(exercises, difficulty):
    # change reps or rest times based on level
<<<<<<< HEAD
    pass
=======
    if difficulty == "easy":
        for exercise in exercises:
            exercise["reps"] = int(exercise["reps"] * 0.5)
    elif difficulty == "hard":
        for exercise in exercises:
            exercise["reps"] = int(exercise["reps"] * 2.0)
    elif difficulty == "medium":
        for exercise in exercises:
            exercise["reps"] = int(exercise["reps"] * 1.0)
    return exercises
>>>>>>> 558d384 (Initial project setup)

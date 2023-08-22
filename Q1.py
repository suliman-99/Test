import datetime


def get_current_info():
    current_date = datetime.datetime.now()

    year = current_date.year
    season = None
    month = current_date.month
    date = current_date.day
    day_of_week = current_date.strftime('%A')

    if 1 <= month <= 3:
        season = "شتاء"
    elif 4 <= month <= 6:
        season = "ربيع"
    elif 7 <= month <= 9:
        season = "صيف"
    else:
        season = "خريف"

    if day_of_week == "Saturday":
        day_of_week = "السبت"
    elif day_of_week == "Sunday":
        day_of_week = "الأحد"
    elif day_of_week == "Monday":
        day_of_week = "الإثنين"
    elif day_of_week == "Tuesday":
        day_of_week = "الثلاثاء"
    elif day_of_week == "Wednesday":
        day_of_week = "الأربعاء"
    elif day_of_week == "Thursday":
        day_of_week = "الخميس"
    else:
        day_of_week == "الجمعة"

    return year, season, month, date, day_of_week


def ask_questions_and_get_answers(user_year, user_season, user_month, user_day_date, user_day):
    year, season, month, date, day_of_week = get_current_info()

    # user_year = input("What year is this? ")
    # user_season = input("What season is this? ")
    # user_month = input("What month is this? ")
    # user_day_date = input("What is today's date? ")
    # user_day = input("What day of the week is this? ")

    correct_answers = {
        "year": str(year),
        "season": season,
        "month": str(month),
        "date": str(date),
        "day_of_week": day_of_week
    }

    results = {
        "a": user_year == correct_answers["year"],
        "b": user_season.lower() == correct_answers["season"].lower(),
        "c": user_month == correct_answers["month"],
        "d": user_day_date == correct_answers["date"],
        "e": user_day.lower() == correct_answers["day_of_week"].lower()
    }

    score = 0

    print("\nQ1 Results:")
    for question, correct in results.items():
        print(f"Question {question}: {'Correct' if correct else 'Incorrect'}")
        if correct:
            score += 1

    return score
# if __name__ == "__main__":
#     results = ask_questions_and_get_answers()
#
#     print("\nResults:")
#     for question, correct in results.items():
#         print(f"Question {question}: {'Correct' if correct else 'Incorrect'}")

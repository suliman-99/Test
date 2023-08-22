def compare_location_answers(user_country, user_continent, user_city):
    # Define default answers
    default_country = "سوريا"
    default_continent = "اسيا"
    default_city = "دمشق"

    # Compare user answers with defaults
    compare_result_country = compare_answers(user_country, default_country)
    compare_result_continent = compare_answers(user_continent, default_continent)
    compare_result_city = compare_answers(user_city, default_city)

    # Return comparison results
    return {
        "Country": compare_result_country,
        "continent": compare_result_continent,
        "City": compare_result_city
    }


def compare_answers(user_answer, default_answer):
    return "Correct" if user_answer.lower() == default_answer.lower() else "Incorrect"


def ask_questions_and_get_answers(user_country, user_continent, user_city):
    # Ask questions
    # user_country = input("What country are we in? ")
    # user_continent = input("What continent are we in? ")
    # user_city = input("What city/town are we in? ")

    # Compare answers and get results
    comparison_results = compare_location_answers(user_country, user_continent, user_city)

    score = 0
    print("\nQ2 Results:")
    # Display comparison results
    for location, result in comparison_results.items():
        print(f"{location}: {result}")
        if result == "Correct":
            score += 1

    return score
# if __name__ == "__main__":
#     main()

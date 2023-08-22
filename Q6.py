def check_wristwatch_response(response):
    correct_responses = ["ساعة", "ساعة يد", "ساعه", "ساعه يد"]

    if response.strip().lower() in correct_responses:
        return 1
    else:
        return 0


# # Example usage
# user_response = input("What is this called? ")
#
# if check_wristwatch_response(user_response):
#     print("Correct response! You scored one point.")
# else:
#     print("Incorrect response.")

def check_pencil_response(response):
    correct_response = "قلم رصاص"

    if response.strip().lower() == correct_response:
        return 1
    else:
        return 0


# # Example usage
# user_response = input("What is this called? ")
#
# if check_pencil_response(user_response):
#     print("Correct response! You scored one point.")
# else:
#     print("Incorrect response.")

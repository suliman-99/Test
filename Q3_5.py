def check_for_target_words(input_text):
    target_words1 = ["كرة", "رجل", "تفاح"]
    target_words2 = ["شجرة", "منزل", "خاتم"]
    target_words3 = ["كرسي", "زهرة", "كلب"]
    # input_text = input("Enter a text: ")
    words_in_text = input_text.split()  # Split the text into words

    found_words = []

    for word in words_in_text:
        cleaned_word = word.strip(".,!?()[]{}\"'")  # Remove common punctuation
        if cleaned_word.lower() in target_words1 or target_words2 or target_words3:
            found_words.append(cleaned_word.lower())

    if len(found_words):
        return 1
    else:
        return 0

# # Example usage
#
# found_words = check_for_target_words(input_text, target_words)
#
# if found_words:
#     print("Found target words:", found_words)
# else:
#     print("No target words found in the text.")

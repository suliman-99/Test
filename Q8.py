def compare_sentences(input_sentence):
    # input_sentence = input("Enter a sentence: ")
    set_sentence1 = "لا تحتوي إلا ولا حتى"
    set_sentence2 = "لا تحتوي الا ولا حتى"

    if input_sentence == set_sentence1 or input_sentence == set_sentence2:
        print("Match")
        return 1
    else:
        print("No Match")
        return 0



# # Example usage
# input_sentence = input("Enter a sentence: ")
# set_sentence = "This is a set sentence."
#
# comparison_result = compare_sentences(input_sentence, set_sentence)
# print("Comparison result:", comparison_result)

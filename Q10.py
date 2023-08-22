import tensorflow_hub as hub
import tensorflow_text
import tensorflow as tf


def check_sentence_meaning(sentence):
    # sentence = input("Enter a sentence: ")

    embed = hub.load("Assets/USE")
    sentence_embedding = embed([sentence])

    SentenceCLF = tf.keras.models.load_model("Assets/modelCNN.keras")
    SentenceCLF.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Set the threshold for meaningfulness
    threshold = 0.5

    # Check if the sentence has meaning
    prediction = SentenceCLF.predict(sentence_embedding)
    if prediction > threshold:
        print(sentence, "\nThe sentence has meaning.")
        return 1
    else:
        print(sentence, "\nThe sentence lacks meaning.")
        return 0

# # Example usage
# sentence_to_check = "This is a meaningful sentence."
# check_sentence_meaning(sentence_to_check)

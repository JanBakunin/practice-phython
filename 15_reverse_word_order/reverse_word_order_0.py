def reverse_string(sentence):
    words = sentence.split()
    reverse = " ".join(words[::-1])
    print(reverse)
reverse_string(input("Enter a sentence: "))
    
def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")

    return cleaned_text == cleaned_text[::-1]


word = "Madam"

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")

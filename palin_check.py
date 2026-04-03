def is_palindrome(user_input):
    corrected_text = ""
    for character in user_input:
        if character.isalnum():
            corrected_text += character.lower()
    if corrected_text == corrected_text[::-1]:
        return True
    else:
        return False
word = "word isi drow"
if is_palindrome(word) == True:
    print("Word is palindrome"
    )
else:
    print("Word is not palindrome")

    
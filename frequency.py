# Input the sentence for the function
u_input = str(input("Input a sentence:"))
def check_frequency(user_input):
    # Using split() to split any white space
    word = user_input.split();
    # Creating frequency as a dictionary to store the keys and values
    frequencies = {}
    #Running a loop to make all character lowercase and removing :;?!. symbols
    try:
        for wor in word:
            word2 = wor.lower().strip(":;?!.")
            # If the new word is in frequency dict. +1 else if not then the frequency will be 1 because there is already a instance in the input.
            if word2 in frequencies:
                frequencies[word2] = frequencies[word2] + 1
            else:
                frequencies[word2] = 1
        return frequencies
    except TypeError:
        print("There is a error in this code")
try:
    # Running the function using the user's input as the parameter of user_input
    result = check_frequency(u_input)
    # Checking if result is a dictionary or not
    if isinstance(result, dict):
        # Will run if result is dictionary
        print("\nFrequency counts:")
        # Show the frequency
        for word in result:
            count = result[word]
            print(f"{word}: {count}")
except TypeError:
    print("Something is wrong in the code") 
    
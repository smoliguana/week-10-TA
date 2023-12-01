#problem 1
def find_linking_subword(word1, word2):
    len_word1 = len(word1)
    len_word2 = len(word2)

    # Find the minimum length to iterate over
    min_len = min(len_word1, len_word2)

    # Iterate from the beginning to find the longest subword
    linking_subword = ''
    for i in range(1, min_len + 1):
        if word1[-i:] == word2[:i]:
            linking_subword = word1[-i:]
    
    return linking_subword

def word_linking_game():
    # Input the first word
    word1 = input("First word: ")
    print("First word :", word1)
    length_word1 = len(word1)
    print("Length of first word:", length_word1)

    # Input the second word
    word2 = input("Second word: ")
    print("Second word :", word2)
    length_word2 = len(word2)
    print("Length of second word:", length_word2)

    # Check if the words can be linked
    linking_subword = find_linking_subword(word1, word2)

    if linking_subword:
        print(f"Both words can be linked with the subword '{linking_subword}'.")
    else:
        print("Both words cannot be linked.")

# Run the word linking game
word_linking_game()


#problem 2
def is_beautiful(number):
    # Check if all digits are the same and not equal to zero
    return len(set(str(number))) == 1 and '0' not in str(number)

def find_smallest_beautiful_number(x):
    # Start from x and check multiples until a beautiful number is found
    multiple = x
    while not is_beautiful(multiple):
        multiple += x
    return multiple

def main():
    try:
        x = int(input("Enter a number (not divisible by 2 and 5): "))
        if x % 2 != 0 and x % 5 != 0:
            result = find_smallest_beautiful_number(x)
            print(f"The smallest beautiful number divisible by {x} is: {result}")
        else:
            print("Please enter a number that is not divisible by 2 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

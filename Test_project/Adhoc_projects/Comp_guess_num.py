import random

'''
    let the computer guess and print the value. And ask the user if the guess is correct.
    if the answer is l:
        the computer will guess again with the updated lower limit
    elif the answer is h:
        computer will guess again with updated lower limit
    elif the answer is c:
        computer will print victory message
'''

def guess_num(x):
    low = 0
    high = x
    prompt = ''   # options are l,h,c  
    while prompt != 'c':
        guess = random.randint(low,high)
        prompt = input(f"Is the guess {guess} correct? Type c for correct, l for low and h for high: ").lower()
        if prompt == 'h':
            high = guess - 1            
        elif prompt == 'l':
            low = guess + 1
    print(f"You guessed correct number {guess}. Congratulations!!")


def main():
    high_limit = int(input("Enter the high limit for computer guessing game: "))
    guess_num(high_limit)

main()
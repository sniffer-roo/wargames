#!/usr/bin/env python3


def replacer(original_text, changes):
    """Function that replaces a given text with
    the swaps defined by the user"""
    final_text = "".join([changes.get(c, c) for c in original_text])
    print(final_text)


text = input('Please put here the text to swap: ').upper()

print('\nNow enter all the swaps you want in the following format: letter, letter to swap. \n\
    E.g: "a e". If you want to remove a swap pair, re-ad the first letter; to remove the\n\
    example pair, just add "a". If you want to stop, input 0, or 1 to clear the swap list.\n')

swaps = {}
while True:
    while True:
        # Require input
        while True:
            letters = input('> Enter swap:').upper()
            # Strip chars in a more or less efficient way
            letters = ''.join([i for i in letters if i.isalpha() | i.isnumeric()])
            # If input is a sole letter, ask again.
            if len(letters) > 1 or letters.isnumeric():
                break
        # If the input is a number...
        if letters.isnumeric():
            # Clear or break
            if letters == '1':
                swaps.clear()
            else:
                break
        # Else, if either one of the inputs is already in the dict
        elif letters[0] in swaps.keys() or letters[1] in swaps.values():
            # If it's among key, grab it
            if letters[0] in swaps.keys():
                replaceKey = repeated = letters[0]
            # If it is not, check the values
            else:
                for key, value in swaps.items():
                    # If it is in the values, grab both
                    if value == letters[1]:
                        repeated, replaceKey = letters[1], key
                        break

            # Present repeated value, ask for proceedure
            print(repeated, 'is already associated to a swap.')
            option = input('Do you want to (r)eplace it or (d)elete it? ').lower()
            # Delete
            if option.startswith('d'):
                del swaps[letters[0]]
            # Replace
            else:
                swaps[replaceKey] = letters[1]
        # It's not in the keys nor the values so it gets added
        else:
            swaps[letters[0]] = letters[1]

        # Print available swaps
        print(swaps)
        # When exit, print text
    replacer(text, swaps)  # Keep on?
    retry = input('(C)ontinue or (E)xit?').lower()
    if retry != 'c':
        break
    else:
        keep = input('Keep the current swap array? (Y)es or (N)o').lower()
        if keep.startswith('N'):
            swaps.clear()

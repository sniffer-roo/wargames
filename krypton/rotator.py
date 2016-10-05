import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase

def caesar(phrase, step):
    result = ''
    for i in phrase:

        case = lower if i.islower() else upper

        if not i.isalpha():
            result += i
        else:
            if mode == 'encrypt':
                result += case[(case.find(i) - step) % 26]
            if mode == 'decrypt':
                result += case[(case.find(i) + step) % 26]
    print('Using shift', step, '> ' + result)


print('Welcome to the rotator!')
while True:
    while True:
        mode = input('Please enter what do you want to do (encrypt or decrypt): ').lower()
        if mode in ('encrypt', 'decrypt'):
            break

    phrase = input('Please enter the word or phrase to be ' + mode + 'ed: ')
    extra = '(entering 0 prints all possible rotations)'
    step = int(input('Please enter the shift to ' + mode + ' ' + extra + ': '))

    if step == 0:
        for i in range(len(lower)):
            caesar(phrase, i);
    else: caesar(phrase, step)

    exit = input('Do you want to perform another ciphering? ')
    if exit in ('No', 'no', 'n', 'N'):
        print('Bye!')
        break
    else:
        print('OK! Here we go again!\n')


if __name__ == '__main__':
    sentence = input('Input a sentence: ')
    print(f'All caps: {sentence.upper()}')
    print(f'All small: {sentence.lower()}')
    print(f'Title case: {sentence.title()}')
    print(f'Case folded sentence {sentence.casefold()}')

    #title conversion
    print(sentence.title())

if __name__ == '__main__':
    sentence = input('Input a sentence: ')
    print('Count of characters :', len(sentence))
    print('Cout of characters (without spaces):', len(sentence.replace(' ', '')))
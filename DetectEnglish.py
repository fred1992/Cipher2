LETTERS_AND_SPACE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
ENGLISH_WORDS = {}
for word in open('dictionary.txt','r'):
    word = word[:-1]
    ENGLISH_WORDS[word] = None

def isEnglish(message, wordPercent=20, letterPercent=85):
    message = message.upper()
    lettersOnly = ''
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly = lettersOnly + symbol   
    
    Words = lettersOnly.split(' ')
    if Words == []:
        return False
   
    count = 0
    for word in Words:
        if word in ENGLISH_WORDS:
            count += 1
    
    wordsMatch = float(count) / len(Words) * 100
    lettersMatch = float(len(lettersOnly)) / len(message) * 100
   
    return wordsMatch >= wordPercent and lettersMatch >= letterPercent




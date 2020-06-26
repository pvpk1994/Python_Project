from collections import Counter
'''
How many sentences can be formed ??
Source:: Interview Question
Author: Pavan Kumar Paluri
'''
counter = 0


def is_anagram(word, list_words):
    global counter
    for a_word in list_words:
        if Counter(a_word) == Counter(word) and a_word != word:
            counter += 2


def countSentences(wordset, sentences):
    global counter
    list_counters = []
    for sentence in sentences:
        counter = 0
        list_sentence_words = sentence.strip().split()
        print(list_sentence_words)
        for word in wordset:
            is_anagram(word, list_sentence_words)
        list_counters.append(counter)
    return list_counters


if __name__ == '__main__':

    wordSet_count = int(input().strip())

    wordSet = []

    for _ in range(wordSet_count):
        wordSet_item = input()
        wordSet.append(wordSet_item)

    sentences_count = int(input().strip())

    sentences = []

    for _ in range(sentences_count):
        sentences_item = input()
        sentences.append(sentences_item)

    print(countSentences(wordSet, sentences))


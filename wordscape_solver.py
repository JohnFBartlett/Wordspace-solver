#!/usr/bin/env python
import sys
import operator


class Solver:
    def __init__(self, letters):
        # init dict
        self.freq_dict = dict()
        with open('SUBTLEX-US_all_words.csv', 'r') as f:
            for line in f.readlines():
                self.freq_dict[line.split(',')[0]] = line.split(',')[-1].rstrip()

        all_words = self.get_words([], {}, letters)
        sorted_words = sorted(all_words.items(), key=operator.itemgetter(1))
        sorted_words.reverse()
        if 'reel' in self.freq_dict:
            print('reel is in it, so yeah')
        print("\n\n\nHere are all the words you can make, sorted by Zipf value (frequency)")
        for thing in sorted_words:
            print(thing)

    def get_words(self, curr_word, words, letters):
        # print("called" + str(words))
        curr_string = ''.join(curr_word)
        # print("trying word " + str(curr_string))
        if len(curr_string) > 2 and curr_string in self.freq_dict and curr_string not in words:
            # print("yes")
            words[curr_string] = self.freq_dict[curr_string]
            # curr_word = []
        if letters:
            for letter in letters:
                temp_letters = list(letters)
                temp_letters.remove(letter)
                temp_word = list(curr_word)
                # print('--')
                # print('curr_word:' + str(temp_word))
                # print('remaining letters:' + str(temp_letters))
                temp_word.append(letter)
                new_words = self.get_words(list(temp_word), {}, temp_letters)
                if new_words:
                    words.update(new_words)
        return words

if __name__ == '__main__':
    letter_set = sys.argv[1].split(',')
    print(letter_set)
    solver = Solver(letter_set)

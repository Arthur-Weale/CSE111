"""
==========================================
    Program: Sentences
    Author: Arthur Weale
    Date: 1-15-2025
    Description:
        A Python program that generates simple English sentences.
==========================================
"""
import random

def main ():
    
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

def get_determiner(quantity):
    # """Return a randomly chosen determiner. A determiner is
    # a word like "the", "a", "one", "some", "many".
    # If quantity is 1, this function will return either "a",
    # "one", or "the". Otherwise this function will return
    # either "some", "many", or "the".
    # Parameter
    #     quantity: an integer.
    #         If quantity is 1, this function will return a
    #         determiner for a single noun. Otherwise this
    #         function will return a determiner for a plural
    #         noun.
    # Return: a randomly chosen determiner.
    # """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    #      """Return a randomly chosen noun.
    #   If quantity is 1, this function will
    #   return one of these ten single nouns:
    #       "bird", "boy", "car", "cat", "child",
    #       "dog", "girl", "man", "rabbit", "woman"
    #   Otherwise, this function will return one of
    #   these ten plural nouns:
    #       "birds", "boys", "cars", "cats", "children",
    #       "dogs", "girls", "men", "rabbits", "women"
    #   Parameter
    #       quantity: an integer that determines if
    #           the returned noun is single or plural.
    #   Return: a randomly chosen noun.
    #     """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                "dogs", "girls", "men", "rabbits", "women"]
    words = random.choice(words)
    return words

def get_verb (quantity, tense):
    if tense == "past":
        words = [
                "drank", "ate", "grew", "laughed", "thought",
                "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write"]

    elif tense == "future":
        words = [ "will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk",
                    "will walk", "will write"]
    words = random.choice(words)
    return words

def get_prepositional():
    prepositions = [
            "about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]
    random_preposition = random.choice(prepositions)
    return random_preposition

def get_prepositional_phrase(quantity):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_prepositional()
    return(f"{preposition} {determiner} {noun}")

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity,tense)
    return(f"{str.capitalize(determiner)} {noun} {verb} {get_prepositional_phrase(quantity)} {get_prepositional_phrase(quantity)}.")


main()
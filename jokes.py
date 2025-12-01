import random


# This script provides a random joke from a predefined list of jokes.
def get_joke():
    # List of jokes to choose from
    jokes = [
        "What kind of shoes to frogs wear? Open-toad sandals.",
        "I had a quiet game of tennis today. There was no racket.",
        "I poured some water over a duck's back yesterday."
        " I don't think he cared.",
        "Were did the pumpkins have their meeting? In the gourdroom.",
        "What do you call a French man wearing sandals? Philipe Fallop.",
        "What do you call a sheep who can sing and dance? Lady Ba Ba.",
        "Who won the neck decorating contest? It was a tie.",
        "Dogs can't operate MRI machines. But catscan.",
        "hat do you call a dog who meditates? Aware wolf."
    ]
    # Return a random joke from the list
    return random.choice(jokes)


# Print a random joke
print(get_joke())

# This code prints a pattern of stars based on a given number.
# the given number is 5, it will print a pattern of stars that ascends to 5\
# then back down to 1.
given_number = 5
if given_number == 5:
    stars = "*"
    # Ascending stars from 1 to 5 with the range function
    ascending_stars = range(1, 5 + 1)
    # Descending stars from 4 to 1 with the range function
    descending_stars = range(4, 0, -1)
    # Combine both ascending and descending stars
    combined_stars = list(ascending_stars) + list(descending_stars)
    # Print the pattern of stars
    for i in combined_stars:
        print(stars * i)

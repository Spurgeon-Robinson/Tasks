# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # Corrected variable name from 'k' to 'key'

# Print dictionary values from simpson_catch_phrases


simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh!",  # Corrected typo in the string
                         "maggie": "(Pacifier Suck)"
                         }


print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])
# Didn't use the correct list format for keys.
# Corrected to a list using square brackets


'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

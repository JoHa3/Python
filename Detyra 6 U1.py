def reverseLookup(d, v):
    keys = []
    for key in d:
        if d[key] == v:
            keys.append(key)
    return keys  # return the list, not a single key

def main():
    french_to_english = {
        "le": "the",
        "la": "the",
        "pomme": "apple",
        "chien": "dog"
    }

    result_1 = reverseLookup(french_to_english, "the")
    print(f'The French words for "the" are: {result_1}')
    print("Expected: ['le', 'la']")
    print()

    result_2 = reverseLookup(french_to_english, "apple")
    print(f'The French word for "apple" is: {result_2}')
    print("Expected: ['pomme']")
    print()

    result_3 = reverseLookup(french_to_english, "dog")
    print(f'The French word for "dog" is: {result_3}')
    print("Expected: ['chien']")
    print()

if __name__ == "__main__":
    main()

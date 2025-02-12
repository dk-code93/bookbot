book_path = 'books/frankenstein.txt'
with open(book_path) as f:
    print(f"--- Begin report of {book_path} ---")
    file_contents = f.read().lower()
    
    all_characters = len(file_contents.split())
    print(f"{all_characters} words found in the document\n")

    character_count = {}
    
    for character in file_contents:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    for key in character_count:
        if key in 'qwertyuiopasdfghjklzxcvbnm':
            print(f"The '{key}' character was found {character_count[key]} times")

    print(f"\n--- End report ---")
    
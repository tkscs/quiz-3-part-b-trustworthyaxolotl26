def check_palendrome():
    word = input("what would you like to check for palendrome-ness: ")
    spot = 0
    for letter in word:
        spot += 1
        if word[spot] == word[-spot-1]:
            return True
        else:
            return False
print()
print(f"it is *{check_palendrome()}* that your word is a palendrome")
print()
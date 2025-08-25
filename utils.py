class UniqueChars():
    
    def first_unique_char(input_string): # return index of first non-repeating char
        found_characters = []
        index = 0

        for letter in input_string:

            if letter in found_characters or index == 0:
                found_characters.append(letter)
                index += 1

            else:
                return index
            
        return -1

# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower-case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become ("1234567A", "_ext_to_te_t")

def process_text(text: str):
    my_tuple = ()
    text_splitted = text.split(sep=' ', maxsplit=1)
    text_splitted[0] = text_splitted[0].upper()
    print('first half:', text_splitted[0])
    for i in text_splitted[1]:
        if i.islower() is False:
            text_splitted[1] = text_splitted[1].replace(i, '_')
    print('Second half:', text_splitted[1])
    my_tuple = tuple(text_splitted)
    return my_tuple


print(process_text('1234567a Text to te5t'))



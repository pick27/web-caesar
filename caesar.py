import string

def alphabet_position(letter):
    """
    Returns the zero based position of the letter entered
    """
    upper_a = ord("A")
    lower_a = ord("a")
    ord_letter = ord(letter)
    if ord_letter >= lower_a:
        answer = ord_letter - lower_a
    else:
        answer = ord_letter - upper_a
    return answer

def rotate_character(char,rot):
    """
    Returns the character rot positions to the right of the char
    """
    upper_a = ord("A")
    lower_a = ord("a")
    if char in string.ascii_lowercase:
        ans = lower_a
    elif char in string.ascii_uppercase:
        ans = upper_a
    else:
        return char
    start = alphabet_position(char)
    spot = (start + rot) % 26
    ord_char = ord(char)
    answer = chr(ans + spot)
    return answer

def encrypt(text,rot):
    """
    Encrpt using Caesar cipher
    """
    answer = ""
    for ch in text:
        answer += rotate_character(ch,rot)
    return answer


class CaesarCipher:
    def __init__(self, key=None):
        if key is None:
            key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j",
                   "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q",
                   "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x",
                   "v": "y", "w": "z", "x": "a", "y": "b", "z": "c", " ": " "}
        self.key = key
        self.antikey = {v: k for k, v in key.items()}

    def encrypt_string(self, string):
        self.check_input(string)
        return ''.join(self.key.get(char, char) for char in string.lower())

    def decrypt_string(self, string):
        self.check_input(string)
        return ''.join(self.antikey.get(char, char) for char in string.lower())

    def check_input(self, string):
        if not all(char.isalpha() or char.isspace() for char in string):
            raise ValueError("Input should only contain alphabets and spaces.")

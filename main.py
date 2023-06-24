import entries


class Vigenere:
    def __init__(self, text):
        self.encrypted = text
        self.decrypted = ""
        self.key = [-19, -3, -17, 0, -2, -7, -4, -13, -1, -11, -20]
        self.state = False

    def decrypt(self):
        if not self.state:
            self.state = True
            self.key_find()

        key_index = 0
        alphabet_lower = "abcdefghijklmnopqrstuvwxyzäöüß"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"

        self.decrypted = ""
        for c in self.encrypted:
            if c in alphabet_lower:
                index = alphabet_lower.index(c)
                shift = self.key[key_index % len(self.key)]
                self.decrypted += alphabet_lower[(index + shift) % len(alphabet_lower)]
                key_index += 1
            elif c in alphabet_upper and c != "ß":
                index = alphabet_upper.index(c)
                shift = self.key[key_index % len(self.key)]
                self.decrypted += alphabet_upper[(index + shift) % len(alphabet_upper)]
                key_index += 1
            else:
                self.decrypted += c
        return self.decrypted

    def key_find(self):
        helper = Vigenere(text=self.encrypted[:15])
        helper.state = True
        while "Abadius" not in helper.decrypt():
            helper.key.append(helper.key[0])
            helper.key.pop(0)
        self.key = helper.key


def export_all():
    exp = ""
    for entry in entries.text_list:
        enc = Vigenere(text=entry)
        exp += enc.decrypt()
        file = open("out/decrypted.txt", "w")
        file.write(exp)


def main():
    sample = Vigenere(text=entries.text1)
    print(sample.decrypt())



if __name__ == "__main__":
    main()

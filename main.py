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

        self.decrypted = ""
        key_index = 0
        alphabet_lower = "abcdefghijklmnopqrstuvwxyzäöüß"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"

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
        container = []

        for i in range(len(self.key)):
            self.key.append(self.key[0])
            self.key.pop(0)
            container.append(self.key[:])
            print(f"Key: {i}\t{self.key}  |  Text: {self.decrypt()[0:25]}")
        num = int(input("Please insert matching number: "))
        print("\n")

        self.key = container[num]

def main():
    t1 = Vigenere(entries.text3)
    print(t1.decrypt())

if __name__ == "__main__":
    main()
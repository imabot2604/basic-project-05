import random, string
def generate(length=8):
    return "".join(random.choices(string.ascii_letters, k=length))
if __name__ == "__main__":
    print("Generated password:", generate())

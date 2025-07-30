try:
    words: list = list()
    with open("LICENSE", "r") as f:
        x:list = f.readlines()

        print(f"No of Lines: {len(x)}")

        f.seek(0)

        for line in x:
            words.extend(line.split())

        print(len(words))

        print(words)
        print(x)
except:
    print("Error")
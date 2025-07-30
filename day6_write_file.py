def write_to_file(filename:str, items: list):
    with open(filename, 'a+') as f:
        for item in items:
            f.write(item)
            f.write("\n")

def read_file(filename:str):
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                print(line)          
    except FileNotFoundError:
        print("Check File Name")  



write_to_file("test.txt", ["a", "b", "c", "d", "e"])

read_file("test.txt")
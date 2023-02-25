def read_files(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


filenames = ["chapter_10\\cats.txt", "chapter_10\\monkeys.txt", "chapter_10\\dogs.txt"]
for filename in filenames:
    read_files(filename)

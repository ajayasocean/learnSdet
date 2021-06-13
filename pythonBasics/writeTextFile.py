file1 = open('testTextFile.txt')
with open('testTextFile.txt', 'r') as reader:  # read mode
    content = reader.readlines()
    for line1 in content:
        print(line1)
    reversed_content = reversed(content)
    for line2 in reversed_content:
        print(line2)
    with open('testTextFile.txt', 'w') as writer:  # write mode
        w_reversed_content = reversed(content)
        for line3 in w_reversed_content:
            print(line3)
            writer.write(line3)
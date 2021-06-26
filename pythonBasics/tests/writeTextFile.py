# file1 = open('../config/testTextFile.txt')
with open('../config/testTextFile.txt', 'r') as reader:  # read mode
    content = reader.readlines()
    for every_line in content:
        print(every_line)
    reversed_content = reversed(content)
    for every_reversed_line in reversed_content:
        print(every_reversed_line)
    with open('../config/testTextFile.txt', 'w') as writer:  # write mode
        w_reversed_content = reversed(content)
        for every_to_write in w_reversed_content:
            print(every_to_write)
            writer.write(every_to_write)

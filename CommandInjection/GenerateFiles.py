path = input("What is the path for file generation?:")

for i in range(0, 6):
    f = open(path + "/text%d.txt" % (i + 1), "w+")
    for k in range(0, 10):
        f.write("This is line %d\n" % (k + 1))

    f.close()

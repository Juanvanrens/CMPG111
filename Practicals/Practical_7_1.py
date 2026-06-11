try:
    file = open("concert_artist.txt","r")

    next_line = file.readline()
    count = 0
    while next_line != "":
        print(next_line.strip())
        next_line = file.readline()
        count += 1

    print(f"\nThere will be {count} artists performing")
    file.close()

except IOError, FileNotFoundError:
    print("File not found")
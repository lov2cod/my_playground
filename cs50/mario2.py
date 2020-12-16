'''
Let’s recreate below pyramid, albeit in text, using hashes (#) for bricks, a la the below.
Each hash is a bit taller than it is wide, so the pyramids themselves are also be taller than they are wide.

   #  #
  ##  ##
 ###  ###
####  ####

'''


def create_pyramid(height):
    for i in range(1, height + 1):
        for j in range(height - i):
            print(" ", end="")
        print(i * "#", end="")
        print("  ", end="")
        print(i * "#", end="")
        print("")
    return 0


def main():
    while True:
        height = int(input("Enter the height of the pyramid:"))
        if 1 <= height <= 8:
            break
    create_pyramid(height)


if __name__ == '__main__':
    main()

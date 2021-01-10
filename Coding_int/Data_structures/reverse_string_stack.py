
from Coding_int.Data_structures.stack import Stack

def reverse_string():
    result = ""
    name = input("Enter the name:")
    ss = Stack()
    for letter in name:
        ss.push_item(letter)
    while ss.size != 0:
        result = result + ss.pop_item()
    print(result)


def main(): reverse_string()


if __name__ == '__main__':
    main()


import csv

sub_data = {}


def size_of_data():
    return len(sub_data)


def update_data(sub_id,new_value):
    if sub_id in sub_data:
        sub_data[sub_id] = new_value
    return sub_data


def add_data(sub_id, value):
    if sub_id not in sub_data:
        sub_data[sub_id] = value
        print(f"Sub ID:{sub_id} appended")
        return sub_data
    else:
        print(f"Sub ID:{sub_id} is already present , so updating the value")
        return update_data(sub_id, value)

def print_data():
    for key, value in sub_data.items():
        print(f"{key}         {value}")
        if value == "Num_trees":
            print("___________________________")


def main():
    with open("treeorder.csv",'r') as data:
        reader = csv.reader(data)
        for row in reader:
            sub_data[row[0]] = row[1]
    print_data()


if __name__ == "__main__": main()

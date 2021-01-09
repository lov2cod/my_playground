import csv


def main():
    data_set = {}
    list_205 = []
    with open("treeorder.csv", "r") as f:
        reader = csv.reader(f)
        data_set = {k:int(v) for k,v in reader}
    print(data_set)



if __name__ == '__main__': main()
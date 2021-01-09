

import csv

def main():
    data_set = {}
    list_205 = []
    with open("treeorderssubsetnodupes.csv","r") as f:
        reader = csv.reader(f)
        for data in reader:
            if data[0] == 'Subdivision_id' or data[1] == 'Num_trees':
                continue
            else:
                if data[0] not in data_set:
                    data_set[data[0]] = int(data[1])
                else:
                    data_set[data[0]] += int(data[1])
    print(data_set)

    
if __name__ == '__main__': main()

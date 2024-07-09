# File to convert a TCG player export to a moxfield csv import
# TODO: add command line args to both pickup and output to files of
#       choice. Additionally, add an option to convert the other
# #     way potentially.

# Note that there is no foil information given, so any information on that
#      is lost in this process...

# Assumes near mint and english cards

def gather_data(data_file : str):
    """
        Gather data from the input file and write it into a dict. Returns a
        dict of the info gathered.
    """
    data = {}
    
    with open(data_file) as f:
        i = 0
        for line in f:
            num, rest = line.split(" ", 1)
            name, set = rest.split("[", 1)
            try:
                data[(name[:-1], set[:-2])] += int(num)
            except:
                data[(name[:-1], set[:-2])] = int(num)
    
    return data
    

def main():
    data = gather_data("data.txt")
    with open("out.csv", "w") as f:
        print('"Count","Name","Edition","Condition","Language","Foil","Collector Number","Alter","Proxy","Purchase Price"', file = f)
        for (name, set) in data.keys():
            if "(" in name:
                print(f'"{data[(name, set)]}","{name.split("(")[0][:-1]}","{set.lower()}","Near Mint","English","","","","",""', file = f)
            # print(f'"{data[(name, set)]}","{name}","{set.lower()}","Near Mint","English","","","","",""', file = f)

if __name__ == "__main__":
    main()
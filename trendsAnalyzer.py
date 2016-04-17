import glob, os


def main():
 
    path = "./output"

    os.chdir(path)
    p = open("../cardsToBuy.txt", "w")

    for file in glob.glob("*.csv"):
        
        f = open(file,"r")

        lines = f.readlines()
        f.close()


        for idx, line in enumerate(lines):
            lines[idx] = line.strip().split(",")

        try:        
                if lines[-3][1] == "100" or lines[-2][1] == "100" or lines[-3][1] == "100":
                        p.write(file+"\n")
        except:
                print(file + " is empty")


if __name__ == "__main__":
    main()

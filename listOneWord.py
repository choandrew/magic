import glob, os


def main():
 
    f = open("./listFutureOOR.py", "r")

        
    lines = f.readlines()
    f.close()

    
    notOneWord = [line for line in lines if len(line.strip().split()) > 1]
    p = open("./listOneWord.txt", "w")

    for line in notOneWord:
        p.write(line)



if __name__ == "__main__":
    main()

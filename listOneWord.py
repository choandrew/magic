import glob, os


def main():
 
    f = open("./listFutureOOR.txt", "r")

        
    lines = f.readlines()


    
    notOneWord = [line for line in lines if len(line.strip().split()) > 1]
    p = open("./listOneWord.txt", "w")

    for line in notOneWord:
        p.write(line)


    f.close()
    p.close()

if __name__ == "__main__":
    main()

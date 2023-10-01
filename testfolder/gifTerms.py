import json

filename = "testfolder/config.json"

def gifTerms(argv):
    # prints list of term keys
    if len(argv) == 2:
        try:
                file = open(filename, 'r')
        except: 
            print("No query terms found.")
        else:
            try:
                contents = json.load(file)
            except:
                file.close()
                print("No query terms found.")
            else:
                file.close()
                keys = list(contents)
                if len(keys):
                    print(list(contents))
                else:
                    print("No query terms found.")

    # removes term key from config.json
    elif len(argv) > 3 and argv[2] == '-D':
        print("Do stuff")

    elif len(argv) == 3 and argv[2] == '-D':
        print("Str value expected. Ex: py . -c -D {term}")
        
    elif len(argv) > 2 and argv[2] != '-D':
        print(f"Unknown flag: {argv[2]}")


if __name__ ==  '__main__':
    gifTerms(['.','-c'])
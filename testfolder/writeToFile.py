import json

filename = "testfolder/config.json"

class WriteToFile:
    def unique(self,content):
        # insert the list to the set
        list_set = set(content)
        # convert the set to the list
        return (list(list_set))
    
    def readFile(self):
        try:
            file = open(filename, 'r')
        except: 
            file = open(filename, 'x')
            file.close()
            return {}
        else:
            try:
                contents = json.load(file)
            except:
                file.close()
                return {}
            else:
                file.close()
                return contents

    def writeFile(self,data,term):
        contents = self.readFile()
        try:
            termContents = contents[term]
        except: 
            contents[term] = data
        else:
            contents[term] = self.unique([*termContents,*data])
        file = open(filename, 'w')
        file.write(json.dumps(contents))
        file.close()


    def __init__(self, data,term):
        self.writeFile(data,term)

if __name__ ==  '__main__':
    WriteToFile(['b'],"dog")